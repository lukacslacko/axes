import json,html,hashlib
from pathlib import Path
P=Path('.');A=json.loads(Path('work/jumble_atlas.json').read_text())
standard=[f for f in A['families'] if f.get('scope','global')=='global' and f['key']!='jumble']
local=[f for f in A['families'] if f not in standard]
limit=max(len(f['axes']) for f in standard)
regimes=sum(v['kind']=='regime' for f in standard for v in f['variants'])
pending=sum(v.get('orbitStatus')=='regular-only' for f in A['families'] for v in f['variants'])
for family in A['families']:
 for case in family['variants']:
  if family['key']!='jumble':
   case.pop('orbitUpperBound',None);case.pop('anchoredPieces',None)
   if case.get('restoringLoops'):case['orbitMethod']='Verified ordinary permutations and legal partial-turn restoring loops; completeness/bounds recorded separately'
nav=[];sections=[]
fmt=lambda a:f'{a:.3f}'.rstrip('0').rstrip('.')+'°'
for fi,f in enumerate(A['families']):
 f['name']=f['name'].split(' · ',1)[-1];name=f['name'];key=f['key']
 nav.append(f'<a href="#{key}"><span>{len(f["axes"]):02}</span>{html.escape(name)}</a>')
 cards=[]
 for vi,v in sorted(enumerate(f['variants']),key=lambda x:x[1]['angle']):
  ident=f'{key}-{vi}';kind=v['kind'];orbits=v['orbits'];angle=fmt(v['angle'])
  title=f'Regime {v["regime"]}' if kind=='regime' else {'zero':'Vanishing cut','central':'Central cut','transition':'Critical depth'}[kind]
  subtitle=f'{fmt(v["low"])} < α < {fmt(v["high"])}' if kind=='regime' else ('All cuts disappear' if kind=='zero' else 'α = '+angle)
  note='Representative depth · α = '+angle if kind=='regime' else ('Zero-area pieces omitted' if kind=='transition' else 'Opposite rays also turn' if kind=='central' else 'One uncut body')
  if v['rays']>limit:note+=f' · {v["rays"]} rays: exceeds {limit}-axis limit'
  if key=='jumble':note+=' · numerical move classes at this angle'
  if v.get('extraSwitches'):note+=' · partial-turn switches; colors at shown depth'
  uncertain=v.get('orbitStatus')=='regular-only'
  class_count=(f'{len(v["geometricUpperBound"])}–{len(orbits)}' if 'geometricUpperBound' in v else f'≤ {len(orbits)}') if uncertain else str(len(orbits))
  uncertainty='<p class="orbit-warning">Approximate groups: same colors are verified reachable; different colors may still merge. <a href="#orbit-bounds">About the bounds</a></p>' if uncertain else ''
  cards.append(f'''<article class="puzzle" id="{ident}" data-family="{fi}" data-variant="{vi}">
    <header><div><a class="case-title" href="#{ident}">{title}</a><p class="interval">{subtitle}</p></div><span class="depth">{angle}</span></header>
    <div class="sphere"><img src="assets/previews/{ident}.png" width="440" height="360" loading="lazy" decoding="async" alt="{html.escape(name)} at {angle}, colored by legal-move class"><canvas width="1" height="1" tabindex="0" role="img" aria-label="{html.escape(name)}, {title}, {angle}. Drag or use arrow keys to rotate; tap a piece to highlight its class."></canvas></div>
    <div class="card-tools"><span><strong>{v['count']}</strong> pieces · <strong>{class_count}</strong> classes</span><button class="reset" title="Reset this view" aria-label="Reset {html.escape(name)}, {title}">Reset view</button></div>
    <div class="legend" aria-label="Reachable piece classes"></div>
    <p class="detail" aria-live="polite">Select a piece or color to inspect its class.</p>
    {uncertainty}
    <p class="case-note">{note}</p>
    </article>''')
 desc= ('Three rays at mutual 60°. Partial turns can unblock a different axis while blocking another.' if key=='jumble' else f'{len(f["axes"])} directed axes · '+str(sum(v['kind']=='regime' for v in f['variants']))+' open depth regimes')
 if f in local:desc+=' · beyond the global-symmetry rule'
 if key=='dodeca':desc+=' · <a href="https://github.com/lukacslacko/axes/blob/main/docs/larger-configurations.md">Irrational-angle partial turns ↗</a>'
 sections.append(f'<section class="family" id="{key}"><div class="family-heading"><span class="family-index">{fi+1:02}</span><div><h2>{html.escape(name)}</h2><p>{desc}</p></div></div><div class="puzzle-grid">'+''.join(cards)+'</div></section>')
page='''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="theme-color" content="#0b1423"><meta name="description" content="An interactive mathematical atlas of conical twisty puzzles: up to seven directed axes, all cut-depth regimes, and piece colors determined by legal reachability."><title>Axes — an atlas of conical twisty puzzles</title><link rel="icon" href="favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="styles.css"><script type="module" src="app.js"></script></head>
<body><a class="skip" href="#atlas">Skip to puzzles</a>
<aside><a class="brand" href="#top"><svg viewBox="0 0 40 40" aria-hidden="true"><circle cx="20" cy="20" r="16"/><path d="M4 20h32M20 4v32M9 9l22 22M9 31L31 9"/></svg><span>axes<small>THE CONICAL ATLAS</small></span></a><nav aria-label="Axis configurations">'''+''.join(nav)+'''<a class="method-link" href="#method"><span>↳</span>Model &amp; colors</a></nav><div class="sidebar-footer"><a href="https://github.com/lukacslacko/axes">Source on GitHub ↗</a><span>MIT licensed</span></div></aside>
<main id="top"><header class="intro"><p class="eyebrow">A MATHEMATICAL CATALOGUE</p><h1>One sphere. Every cut.</h1><p>Explore conical twisty puzzles with up to seven directed axes. Shared colors are backed by legal turns that carry whole pieces between their positions.</p><div class="atlas-meta"><span>11 standard configurations</span><span>32 open regimes</span><span>@@LOCAL@@ local examples</span></div></header>
<div class="toolbar"><span>Drag any sphere to rotate · Tap a piece to inspect</span><div><label><input type="checkbox" id="show-axes" checked> Axes</label><label><input type="checkbox" id="show-numbers"> Piece IDs</label></div></div>
<p class="reachability-status">@@PENDING@@ cases show conservative color groups: shared colors are verified, but additional mergers may be possible. <a href="#orbit-bounds">What is established?</a></p>
<p class="notice">Depth α is the cone’s half-angle: 0° removes the cuts; 90° cuts through the center. All cases are below, including critical depths and endpoint limits. Colors are local to each sphere; each swatch shows the number of pieces in its class.</p><div id="status" role="status">Loading interactive spheres…</div><noscript><p class="error">Enable JavaScript to rotate and color the spheres. The model and case descriptions remain available below.</p></noscript><div id="atlas">'''+''.join(sections)+'''</div>
<section id="method" class="method"><p class="eyebrow">READING THE ATLAS</p><h2>Axes, sectors, and legal moves</h2>
<div class="method-grid"><div><h3>One ray, one cone</h3><p>An axis is a directed ray from the center. With unit direction <i>u</i>, its moving cap is <span class="formula">u · x &gt; cos α</span> on the unit sphere. Every axis has the same half-angle. Connected regions between the cut circles are separate pieces, even when they lie in the same set of caps.</p><p>The spherical surface shows angular sectors. Imagine a generic asymmetric radial exterior: every piece’s position and orientation matter, even when it shares a color with another piece.</p></div>
<div><h3>What a shared color means</h3><p>A whole piece can be carried into the other piece’s sector by a sequence of legal rigid turns, with its complete cut geometry fitting that slot. We compute reachability from moves, not from visual similarity or the number of neighboring axes.</p><p>Single-piece classes keep their own colors. A shared color does not mean two pieces are interchangeable in a solved asymmetric exterior, or that any arbitrary permutation of a class is achievable.</p></div>
<div><h3>Why these configurations?</h3><p>The eleven standard configurations satisfy a specific rule: every axis admits a nonidentity rotation preserving the entire axis set. This is a finite catalogue under that rule, not an exhaustive list under every possible local rule for twisty puzzles. The separately listed local examples illustrate wider possibilities.</p><p>At 90°, the other half of each cut can turn too. These extra directed axes are counted and shown; endpoints with more than seven axes are explicitly marked.</p></div>
<div><h3>Depths and jumbling</h3><p>Open regimes are separated by tangencies and multiple intersections of cut circles. A representative angle is drawn in each interval; the critical angles have their own cards. Piece counts are checked by the circle arrangement’s Euler characteristic.</p><p>Colors start from ordinary move permutations and include verified sequences of partial turns that restore the cut diagram. Whole-piece geometry is checked throughout. The original three-axis example also uses state-dependent turns; proofs, numerical certificates, and unresolved cases are documented in the source.</p></div></div>
<div id="orbit-bounds" class="local-constructions"><h3>Reachability: verified groups and unresolved mergers</h3><p>In @@PENDING@@ cases, the colors deliberately show conservative groups linked by verified legal turns. Different colors may still merge through additional partial turns. “≤” gives the number of verified groups; a range is shown where a tighter geometric bound is known. Earlier state-search results are preserved, while new cases prioritize extending the geometry catalogue over exhaustive orbit searches.</p><p>The depth intervals classify the initial circle arrangement. Where partial turns occur, move availability may change at additional depths inside an interval; the colors and certificates apply to the angle actually drawn.</p></div>
<div id="local-constructions" class="local-constructions"><h3>Beyond the global rule</h3><p>Twisted polyhedra can support useful conical moves without a rotation symmetry about every vertex. Direct coordinate calculations give these two constructions:</p><div class="table-scroll"><table><thead><tr><th>Vertex rays</th><th>Example</th><th>Cut depth</th><th>Interacting moves</th></tr></thead><tbody><tr><td>8</td><td>Gyrobifastigium</td><td>40°</td><td>Four ordinary half-turn axes; four axes with 98.213° partial turns</td></tr><tr><td>24</td><td>Elongated square gyrobicupola</td><td>25°</td><td>Every axis supports a 64.737° partial turn</td></tr></tbody></table></div><p>A partial turn restores another axis while blocking some others. The eight-ray construction persists as its ridge angles vary continuously. @@LOCALGALLERIES@@</p><p><a href="https://github.com/lukacslacko/axes/blob/main/docs/local-constructions.md">Coordinates, deformation formulas, and checked move witnesses ↗</a></p></div>
<p class="read-more"><a href="https://github.com/lukacslacko/axes/blob/main/docs/catalogue.md">Mathematical catalogue ↗</a><a href="https://github.com/lukacslacko/axes/blob/main/docs/reachability.md">Reachability calculation ↗</a><a href="https://github.com/lukacslacko/axes">Code &amp; reproducible data ↗</a></p></section>
<footer>Axes · A conical twisty-puzzle atlas <a href="LICENSE">MIT License</a></footer></main></body></html>'''
galleries='The <a href="#gyrobifastigium">gyrobifastigium gallery</a> shows all initial cut-arrangement depths with conservative colors.'
if any(f['key']=='gyrobicupola' for f in local):
 galleries='The <a href="#gyrobifastigium">gyrobifastigium</a> and <a href="#gyrobicupola">elongated square gyrobicupola</a> galleries show all initial cut-arrangement depths with conservative colors.'
page=page.replace('@@PENDING@@',str(pending)).replace('@@LOCAL@@',str(len(local))).replace('@@LOCALGALLERIES@@',galleries)
page=page.replace('seven directed axes',str(limit)+' directed axes').replace('seven axes',str(limit)+' axes').replace('11 standard configurations',str(len(standard))+' standard configurations').replace('32 open regimes',str(regimes)+' open regimes').replace('The eleven standard configurations','The '+str(len(standard))+' standard configurations')
(P/'assets/atlas.json').write_text(json.dumps(A,separators=(',',':')))

# A small manifest starts the gallery; detailed sphere data loads on demand.
viewdir=P/'assets/views';viewdir.mkdir(exist_ok=True)
manifest=dict(width=A['width'],height=A['height'],families=[])
for f in A['families']:
 item={k:f[k] for k in ['key','name','axes','scope'] if k in f};item['variants']=[]
 for vi,v in enumerate(f['variants']):
  item['variants'].append({k:v[k] for k in ['angle','count','width','height','labelBytes','orbitStatus'] if k in v})
  fields=['angle','count','data','width','height','labelBytes','pieces','orbits','orbitStatus']
  (viewdir/f"{f['key']}-{vi}.json").write_text(json.dumps({k:v[k] for k in fields if k in v},separators=(',',':')))
 manifest['families'].append(item)
(P/'assets/index.json').write_text(json.dumps(manifest,separators=(',',':')))
digest=lambda path:hashlib.sha256(path.read_bytes()).hexdigest()[:12]
version=digest(P/'assets/atlas.json')
viewer=(P/'app.js').read_text().replace("'./renderer.js'",f"'../renderer.js?v={digest(P/'renderer.js')}'")
viewer=viewer.replace("fetch('./assets/index.json')",f"fetch('./assets/index.json?v={version}')")
viewer=viewer.replace("+'.json')",f"+'.json?v={version}')")
(P/'assets/viewer.js').write_text(viewer)
page=page.replace('src="app.js"',f'src="assets/viewer.js?v={digest(P/"assets/viewer.js")}"')
page=page.replace('href="styles.css"',f'href="styles.css?v={digest(P/"styles.css")}"')
(P/'index.html').write_text('\n'.join(line.rstrip() for line in page.splitlines())+'\n')
