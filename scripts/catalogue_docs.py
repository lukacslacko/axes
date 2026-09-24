import json
from pathlib import Path

A=json.loads(Path('assets/atlas.json').read_text());families=[f for f in A['families'] if f['key']!='jumble']
limit=max(len(f['axes']) for f in families);regimes=sum(v['kind']=='regime' for f in families for v in f['variants']);cases=sum(len(f['variants']) for f in A['families'])
fmt=lambda a:f'{a:.6f}'.rstrip('0').rstrip('.')+'°'
doc=f'''# Complete global-rule catalogue through {limit} axes

The rendered atlas contains **{len(families)} standard configurations, {regimes} open common-angle regimes, and {cases} views** including critical depths, endpoints, and the separate jumbling example. Counts refer to directed rays, not unoriented lines. All configurations are derived from finite rotation groups, without consulting a catalogue of manufactured puzzles.

## Why the enumeration is complete

Let `G` be the entire rotation symmetry group of a finite non-collinear axis set `A`. Its action on `A` is faithful, so `G` is finite. Requiring every ray to support a nonidentity global symmetry forces each ray to be a rotation pole of `G`. Since `A` is `G`-invariant, it is a union of complete pole orbits. The finite subgroups of `SO(3)` give the following possibilities:

- Cyclic: the two poles, giving the single-ray and antipodal-pair degeneracies.
- Dihedral: a polar pair and two equatorial polygon orbits. Either equatorial orbit is a regular polygon; their union is a regular polygon with twice as many vertices. Thus the two infinite families are a regular great-circle ring and a ring together with both poles.
- Tetrahedral: pole orbits of sizes 4, 4, and 6. Besides the tetrahedron and octahedron, the new unions through 12 rays are the cube (4 + 4) and tetrahedron + octahedron (4 + 6). The two choices of tetrahedral 4-orbit give congruent 10-ray configurations, related by a rotation preserving the 6-orbit.
- Octahedral: pole orbits of sizes 6, 8, and 12. No union of two fits under 12. The 6-ray set already occurs as a square plus poles; the cube contributes 8 and the edge directions contribute 12.
- Icosahedral: pole orbits of sizes 12, 20, and 30. Only the 12-ray vertex set fits through 12.

Removing these duplicate descriptions leaves exactly the configurations listed below for the current bound. The argument is for the global-symmetry rule; the weaker local rule and general jumbling geometry are not finite classifications of this sort.

## Rendered configurations and depth regimes

| Rays | Configuration | Critical half-angles | Piece counts in successive open regimes |
|---:|---|---|---|
'''
for f in families:
 critical=[v['angle'] for v in f['variants'] if v['kind']=='transition'];counts=[v['count'] for v in f['variants'] if v['kind']=='regime']
 doc+=f'| {len(f["axes"])} | [{f["name"]}](https://lukacslacko.github.io/axes/#{f["key"]}) | '+(', '.join(map(fmt,critical)) or 'None')+' | '+' → '.join(map(str,counts))+' |\n'
doc+='''
Each pair tangency is at half the angle between its rays. Every consistent triple of circle equations contributes its sphere-incidence angle; duplicate events are merged. Higher-order coincidences are already among these triple events. These events exhaust the changes of a finite equal-radius small-circle arrangement away from the 0° and 90° endpoints. Each open interval is represented by its midpoint in angle, with every critical value also rendered separately.

For a generic angle, `F = 2p + c + 1`, where `p` is the number of intersecting pairs of circles and `c` is the number of components of their intersection graph, including isolated circles. At critical angles the complete incidence graph is used in `F = E - V + C + 1`; the formula does not treat a multiple intersection as several distinct vertices.

Equal piece counts on either side of an event do not imply the same puzzle. Triple incidences can change which cones contain a sector while preserving the total number of sectors. Orientation, incidence, and connected components are retained by the calculation.

The 90° endpoint adds the opposite rays and deduplicates their planes. Some endpoints therefore exceed the catalogue's directed-axis bound; their cards state the full count. They are useful limits of the displayed families, not extra claims of configurations within the bound.

See [the original model and derivation](model.md) and [the reachability calculation](reachability.md) for the angular sector model, legal turns, and numerical limitations.
'''
Path('docs/catalogue.md').write_text(doc)
readme=Path('README.md').read_text();import re
readme=re.sub(r'- Eleven standard axis configurations with at most seven directed rays\.',f'- **{len(families)} standard axis configurations** with at most **{limit} directed rays**.',readme)
readme=re.sub(r'- \*\*\d+ standard axis configurations\*\* with at most \*\*\d+ directed rays\*\*\.',f'- **{len(families)} standard axis configurations** with at most **{limit} directed rays**.',readme)
readme=re.sub(r'- Thirty-two open cut-arrangement regimes, their critical depths, and both endpoints\.',f'- **{regimes} open cut-arrangement regimes**, their critical depths, and both endpoints.',readme)
readme=re.sub(r'- \*\*\d+ open cut-arrangement regimes\*\*, their critical depths, and both endpoints\.',f'- **{regimes} open cut-arrangement regimes**, their critical depths, and both endpoints.',readme)
readme=re.sub(r'\*\*\d+ sphere views\*\*',f'**{cases} sphere views**',readme)
readme=readme.replace('See [the mathematical model]', 'See [the current catalogue and completeness argument](docs/catalogue.md), [the mathematical model]') if 'current catalogue' not in readme else readme
readme=readme.replace('Each card keeps a 2D image and its own camera; the decompressed atlas cache is bounded.','Every card has a pre-rendered mathematical preview and its own camera; live canvas buffers are retained only near the viewport, and the decompressed atlas cache is bounded.')
Path('README.md').write_text(readme)
print(limit,'axis limit;',len(families),'standard configurations;',regimes,'regimes;',cases,'views')
