// Data-format and CPU picking regression checks; no browser is required.
import fs from 'node:fs';
import zlib from 'node:zlib';
import assert from 'node:assert/strict';
import {pieceAt,colors} from '../renderer.js';

const atlas=JSON.parse(fs.readFileSync('assets/atlas.json'));
let checked=0,wide=0;
for(const family of atlas.families){
  for(const variant of family.variants){
    const bytes=zlib.gunzipSync(Buffer.from(variant.data,'base64'));
    const pixels=variant.labelBytes===2?new Uint16Array(bytes.buffer,bytes.byteOffset,bytes.byteLength/2):bytes;
    const masks=new Uint32Array(variant.count+1),fallback=Object.create(null);masks.fill(-1);
    variant.pieces.forEach((p,i)=>{masks[i+1]=p.mask;(fallback[p.mask]??=[]).push(i+1);});
    const state={family,variant,pixels,masks,fallback,width:variant.width||atlas.width,height:variant.height||atlas.height,cut:Math.cos(variant.angle*Math.PI/180)};
    assert.equal(pixels.length,state.width*state.height);
    assert.ok(variant.orbits.length<=colors.length);
    if(variant.count>255){assert.equal(variant.labelBytes,2);wide++;}
    variant.pieces.forEach((p,i)=>{
      const length=Math.hypot(...p.seed),q=p.seed.map(x=>x/length);
      assert.equal(pieceAt(state,q,atlas),i+1,`${family.key} at ${variant.angle}, piece ${i+1}`);checked++;
    });
  }
}
console.log(`Validated ${checked} piece-center selections, including ${wide} views with 16-bit labels.`);
