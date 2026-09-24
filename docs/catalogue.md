# Complete global-rule catalogue through 24 axes

The rendered atlas contains **53 standard configurations, 504 open common-angle regimes, and 1178 views** including critical depths, endpoints, and 3 local examples. Counts refer to directed rays, not unoriented lines. All standard configurations are derived from finite rotation groups, without consulting a catalogue of manufactured puzzles.

## Why the enumeration is complete

Let `G` be the entire rotation symmetry group of a finite non-collinear axis set `A`. Its action on `A` is faithful, so `G` is finite. Requiring every ray to support a nonidentity global symmetry forces each ray to be a rotation pole of `G`. Since `A` is `G`-invariant, it is a union of complete pole orbits. The finite subgroups of `SO(3)` give the following possibilities:

- Cyclic: the two poles, giving the single-ray and antipodal-pair degeneracies.
- Dihedral: a polar pair and two equatorial polygon orbits. Either equatorial orbit is a regular polygon; their union is a regular polygon with twice as many vertices. Thus the two infinite families are a regular great-circle ring and a ring together with both poles.
- Tetrahedral: pole orbits of sizes 4, 4, and 6. Besides the tetrahedron and octahedron, the unions are the cube (4 + 4), tetrahedron + octahedron (4 + 6), and cube + octahedron (4 + 4 + 6). The two choices of tetrahedral 4-orbit give congruent 10-ray configurations, related by a rotation preserving the 6-orbit.
- Octahedral: pole orbits of sizes 6, 8, and 12. The 6-ray set already occurs as a square plus poles; the cube contributes 8 and the edge directions contribute 12. Their unions add configurations at 14, 18, 20, and 26 rays when these fit under the current bound.
- Icosahedral: pole orbits of sizes 12, 20, and 30. Include every union whose size fits under the current bound. The first individual orbits occur at 12 (vertices), 20 (face directions), and 30 (edge directions).

Removing these duplicate descriptions leaves exactly the configurations listed below for the current bound. The argument is for the global-symmetry rule; the weaker local rule and general jumbling geometry are not finite classifications of this sort.

## Rendered configurations and depth regimes

| Rays | Configuration | Critical half-angles | Piece counts in successive open regimes |
|---:|---|---|---|
| 1 | [Single ray](https://lukacslacko.github.io/axes/#one) | None | 2 |
| 2 | [Antipodal pair](https://lukacslacko.github.io/axes/#opposite) | None | 3 |
| 3 | [Triangular ring](https://lukacslacko.github.io/axes/#ring3) | 60° | 4 → 8 |
| 4 | [Square ring](https://lukacslacko.github.io/axes/#ring4) | 45° | 5 → 10 |
| 4 | [Tetrahedral axes](https://lukacslacko.github.io/axes/#tetra) | 54.73561°, 70.528779° | 5 → 14 → 14 |
| 5 | [Pentagonal ring](https://lukacslacko.github.io/axes/#ring5) | 36°, 72° | 6 → 12 → 22 |
| 5 | [Triangle + poles](https://lukacslacko.github.io/axes/#bipyramid3) | 45°, 60°, 63.434949° | 6 → 14 → 20 → 20 |
| 6 | [Hexagonal ring](https://lukacslacko.github.io/axes/#ring6) | 30°, 60° | 7 → 14 → 26 |
| 6 | [Octahedral axes](https://lukacslacko.github.io/axes/#bipyramid4) | 45°, 54.73561° | 7 → 26 → 26 |
| 7 | [Heptagonal ring](https://lukacslacko.github.io/axes/#ring7) | 25.714286°, 51.428571°, 77.142857° | 8 → 16 → 30 → 44 |
| 7 | [Pentagon + poles](https://lukacslacko.github.io/axes/#bipyramid5) | 36°, 45°, 51.026553°, 72°, 72.827962° | 8 → 14 → 32 → 32 → 42 → 42 |
| 8 | [8-gon ring](https://lukacslacko.github.io/axes/#ring8) | 22.5°, 45°, 67.5° | 9 → 18 → 34 → 50 |
| 8 | [6-gon + poles](https://lukacslacko.github.io/axes/#bipyramid6) | 30°, 45°, 49.106605°, 60°, 63.434949° | 9 → 16 → 38 → 38 → 50 → 50 |
| 8 | [Cube vertices](https://lukacslacko.github.io/axes/#cube) | 35.26439°, 54.73561°, 70.528779° | 9 → 26 → 50 → 50 |
| 9 | [9-gon ring](https://lukacslacko.github.io/axes/#ring9) | 20°, 40°, 60°, 80° | 10 → 20 → 38 → 56 → 74 |
| 9 | [7-gon + poles](https://lukacslacko.github.io/axes/#bipyramid7) | 25.714286°, 45°, 47.982133°, 51.428571°, 58.056881°, 77.142857°, 77.454884° | 10 → 18 → 44 → 44 → 58 → 58 → 72 → 72 |
| 10 | [10-gon ring](https://lukacslacko.github.io/axes/#ring10) | 18°, 36°, 54°, 72° | 11 → 22 → 42 → 62 → 82 |
| 10 | [8-gon + poles](https://lukacslacko.github.io/axes/#bipyramid8) | 22.5°, 45°, 47.26579°, 54.73561°, 67.5°, 69.05898° | 11 → 20 → 66 → 66 → 66 → 82 → 82 |
| 10 | [Tetrahedron + octahedron](https://lukacslacko.github.io/axes/#tetra_octa) | 27.367805°, 45°, 45.992973°, 54.73561°, 62.632195°, 63.434949°, 70.528779°, 75.489181° | 11 → 26 → 50 → 50 → 62 → 86 → 86 → 86 → 86 |
| 11 | [11-gon ring](https://lukacslacko.github.io/axes/#ring11) | 16.363636°, 32.727273°, 49.090909°, 65.454545°, 81.818182° | 12 → 24 → 46 → 68 → 90 → 112 |
| 11 | [9-gon + poles](https://lukacslacko.github.io/axes/#bipyramid9) | 20°, 40°, 45°, 46.780821°, 52.54628°, 60°, 63.434949°, 80°, 80.148924° | 12 → 22 → 40 → 74 → 74 → 74 → 92 → 92 → 110 → 110 |
| 12 | [12-gon ring](https://lukacslacko.github.io/axes/#ring12) | 15°, 30°, 45°, 60°, 75° | 13 → 26 → 50 → 74 → 98 → 122 |
| 12 | [10-gon + poles](https://lukacslacko.github.io/axes/#bipyramid10) | 18°, 36°, 45°, 46.436999°, 51.026553°, 54°, 59.553616°, 72°, 72.827962° | 13 → 24 → 44 → 82 → 82 → 82 → 102 → 102 → 122 → 122 |
| 12 | [Cube edge axes](https://lukacslacko.github.io/axes/#cubocta) | 30°, 35.26439°, 45°, 60°, 64.760598°, 71.565051° | 13 → 50 → 50 → 74 → 122 → 122 → 122 |
| 12 | [Icosahedral vertices](https://lukacslacko.github.io/axes/#ico) | 31.717474°, 37.377368°, 58.282526°, 63.434949°, 79.187683° | 13 → 62 → 62 → 122 → 122 → 122 |
| 13 | [13-gon ring](https://lukacslacko.github.io/axes/#ring13) | 13.846154°, 27.692308°, 41.538462°, 55.384615°, 69.230769°, 83.076923° | 14 → 28 → 54 → 80 → 106 → 132 → 158 |
| 13 | [11-gon + poles](https://lukacslacko.github.io/axes/#bipyramid11) | 16.363636°, 32.727273°, 45°, 46.184261°, 49.090909°, 49.927657°, 56.780785°, 65.454545°, 67.441268°, 81.818182°, 81.90035° | 14 → 26 → 48 → 90 → 90 → 112 → 112 → 112 → 134 → 134 → 156 → 156 |
| 14 | [14-gon ring](https://lukacslacko.github.io/axes/#ring14) | 12.857143°, 25.714286°, 38.571429°, 51.428571°, 64.285714°, 77.142857° | 15 → 30 → 58 → 86 → 114 → 142 → 170 |
| 14 | [12-gon + poles](https://lukacslacko.github.io/axes/#bipyramid12) | 15°, 30°, 45°, 45.992973°, 49.106605°, 54.73561°, 60°, 63.434949°, 75°, 75.489181° | 15 → 28 → 52 → 122 → 122 → 122 → 122 → 146 → 146 → 170 → 170 |
| 14 | [Cube vertices + face axes](https://lukacslacko.github.io/axes/#octa_cube) | 27.367805°, 35.26439°, 36.206023°, 45°, 45.992973°, 54.73561°, 62.632195°, 63.434949°, 69.896091°, 70.528779°, 75.489181° | 15 → 50 → 74 → 74 → 98 → 98 → 122 → 170 → 170 → 170 → 170 → 170 |
| 15 | [15-gon ring](https://lukacslacko.github.io/axes/#ring15) | 12°, 24°, 36°, 48°, 60°, 72°, 84° | 16 → 32 → 62 → 92 → 122 → 152 → 182 → 212 |
| 15 | [13-gon + poles](https://lukacslacko.github.io/axes/#bipyramid13) | 13.846154°, 27.692308°, 41.538462°, 45°, 45.844668°, 48.476522°, 53.184751°, 55.384615°, 60.40062°, 69.230769°, 70.475245°, 83.076923°, 83.126916° | 16 → 30 → 56 → 82 → 132 → 132 → 132 → 132 → 158 → 158 → 184 → 184 → 210 → 210 |
| 16 | [16-gon ring](https://lukacslacko.github.io/axes/#ring16) | 11.25°, 22.5°, 33.75°, 45°, 56.25°, 67.5°, 78.75° | 17 → 34 → 66 → 98 → 130 → 162 → 194 → 226 |
| 16 | [14-gon + poles](https://lukacslacko.github.io/axes/#bipyramid14) | 12.857143°, 25.714286°, 38.571429°, 45°, 45.727342°, 47.982133°, 51.428571°, 51.980584°, 58.056881°, 64.285714°, 66.544762°, 77.142857°, 77.454884° | 17 → 32 → 60 → 88 → 142 → 142 → 142 → 170 → 170 → 170 → 198 → 198 → 226 → 226 |
| 17 | [17-gon ring](https://lukacslacko.github.io/axes/#ring17) | 10.588235°, 21.176471°, 31.764706°, 42.352941°, 52.941176°, 63.529412°, 74.117647°, 84.705882° | 18 → 36 → 70 → 104 → 138 → 172 → 206 → 240 → 274 |
| 17 | [15-gon + poles](https://lukacslacko.github.io/axes/#bipyramid15) | 12°, 24°, 36°, 45°, 45.632915°, 47.586881°, 48°, 51.026553°, 56.212308°, 60°, 63.434949°, 72°, 72.827962°, 84°, 84.032631° | 18 → 34 → 64 → 94 → 152 → 152 → 152 → 182 → 182 → 182 → 212 → 212 → 242 → 242 → 272 → 272 |
| 18 | [18-gon ring](https://lukacslacko.github.io/axes/#ring18) | 10°, 20°, 30°, 40°, 50°, 60°, 70°, 80° | 19 → 38 → 74 → 110 → 146 → 182 → 218 → 254 → 290 |
| 18 | [16-gon + poles](https://lukacslacko.github.io/axes/#bipyramid16) | 11.25°, 22.5°, 33.75°, 45°, 45.555784°, 47.26579°, 50.257506°, 54.73561°, 56.25°, 60.944753°, 67.5°, 69.05898°, 78.75°, 78.960806° | 19 → 36 → 68 → 100 → 194 → 194 → 194 → 194 → 194 → 226 → 226 → 258 → 258 → 290 → 290 |
| 18 | [Cube face + edge axes](https://lukacslacko.github.io/axes/#octa_edges) | 22.5°, 30°, 30.361193°, 35.26439°, 45°, 47.26579°, 54.73561°, 60°, 61.924446°, 64.760598°, 67.5°, 67.792346°, 69.05898°, 71.565051°, 73.67505°, 77.54109° | 19 → 50 → 98 → 98 → 98 → 194 → 194 → 194 → 242 → 242 → 242 → 290 → 290 → 290 → 290 → 290 → 290 |
| 19 | [19-gon ring](https://lukacslacko.github.io/axes/#ring19) | 9.473684°, 18.947368°, 28.421053°, 37.894737°, 47.368421°, 56.842105°, 66.315789°, 75.789474°, 85.263158° | 20 → 40 → 78 → 116 → 154 → 192 → 230 → 268 → 306 → 344 |
| 19 | [17-gon + poles](https://lukacslacko.github.io/axes/#bipyramid17) | 10.588235°, 21.176471°, 31.764706°, 42.352941°, 45°, 45.491961°, 47.001313°, 49.628242°, 52.941176°, 53.535268°, 58.925377°, 63.529412°, 65.975634°, 74.117647°, 74.694992°, 84.705882°, 84.728339° | 20 → 38 → 72 → 106 → 140 → 206 → 206 → 206 → 206 → 240 → 240 → 240 → 274 → 274 → 308 → 308 → 342 → 342 |
| 20 | [20-gon ring](https://lukacslacko.github.io/axes/#ring20) | 9°, 18°, 27°, 36°, 45°, 54°, 63°, 72°, 81° | 21 → 42 → 82 → 122 → 162 → 202 → 242 → 282 → 322 → 362 |
| 20 | [18-gon + poles](https://lukacslacko.github.io/axes/#bipyramid18) | 10°, 20°, 30°, 40°, 45°, 45.438549°, 46.780821°, 49.106605°, 50°, 52.54628°, 57.267593°, 60°, 63.434949°, 70°, 71.118279°, 80°, 80.148924° | 21 → 40 → 76 → 112 → 148 → 218 → 218 → 218 → 218 → 254 → 254 → 254 → 290 → 290 → 326 → 326 → 362 → 362 |
| 20 | [Cube vertices + edge axes](https://lukacslacko.github.io/axes/#cube_edges) | 17.632195°, 30°, 32.443079°, 35.26439°, 45°, 46.377969°, 49.106605°, 50.76848°, 54.73561°, 56.024469°, 60°, 63.434949°, 64.760598°, 68.740529°, 70.528779°, 71.565051°, 72.367805°, 73.148154°, 73.897886°, 77.910678°, 80.970145°, 82.950556° | 21 → 50 → 98 → 98 → 122 → 242 → 242 → 242 → 242 → 266 → 266 → 314 → 314 → 314 → 314 → 314 → 314 → 362 → 362 → 362 → 362 → 362 → 362 |
| 20 | [Dodecahedral vertices](https://lukacslacko.github.io/axes/#dodeca) | 20.905157°, 35.26439°, 37.377368°, 41.810315°, 54.73561°, 56.794912°, 60.794068°, 69.094843°, 70.528779°, 79.187683°, 84.54528° | 21 → 62 → 182 → 182 → 182 → 302 → 302 → 302 → 362 → 362 → 362 → 362 |
| 21 | [21-gon ring](https://lukacslacko.github.io/axes/#ring21) | 8.571429°, 17.142857°, 25.714286°, 34.285714°, 42.857143°, 51.428571°, 60°, 68.571429°, 77.142857°, 85.714286° | 22 → 44 → 86 → 128 → 170 → 212 → 254 → 296 → 338 → 380 → 422 |
| 21 | [19-gon + poles](https://lukacslacko.github.io/axes/#bipyramid19) | 9.473684°, 18.947368°, 28.421053°, 37.894737°, 45°, 45.393396°, 46.595032°, 47.368421°, 48.66922°, 51.721599°, 55.890939°, 56.842105°, 61.323627°, 66.315789°, 68.114898°, 75.789474°, 76.207461°, 85.263158°, 85.279263° | 22 → 42 → 80 → 118 → 156 → 230 → 230 → 230 → 268 → 268 → 268 → 268 → 306 → 306 → 344 → 344 → 382 → 382 → 420 → 420 |
| 22 | [22-gon ring](https://lukacslacko.github.io/axes/#ring22) | 8.181818°, 16.363636°, 24.545455°, 32.727273°, 40.909091°, 49.090909°, 57.272727°, 65.454545°, 73.636364°, 81.818182° | 23 → 46 → 90 → 134 → 178 → 222 → 266 → 310 → 354 → 398 → 442 |
| 22 | [20-gon + poles](https://lukacslacko.github.io/axes/#bipyramid20) | 9°, 18°, 27°, 36°, 45°, 45.354883°, 46.436999°, 48.298754°, 51.026553°, 54°, 54.73561°, 59.553616°, 63°, 65.582403°, 72°, 72.827962°, 81°, 81.109024° | 23 → 44 → 84 → 124 → 164 → 282 → 282 → 282 → 282 → 282 → 322 → 322 → 322 → 362 → 362 → 402 → 402 → 442 → 442 |
| 23 | [23-gon ring](https://lukacslacko.github.io/axes/#ring23) | 7.826087°, 15.652174°, 23.478261°, 31.304348°, 39.130435°, 46.956522°, 54.782609°, 62.608696°, 70.434783°, 78.26087°, 86.086957° | 24 → 48 → 94 → 140 → 186 → 232 → 278 → 324 → 370 → 416 → 462 → 508 |
| 23 | [21-gon + poles](https://lukacslacko.github.io/axes/#bipyramid21) | 8.571429°, 17.142857°, 25.714286°, 34.285714°, 42.857143°, 45°, 45.321767°, 46.301436°, 47.982133°, 50.435162°, 51.428571°, 53.756651°, 58.056881°, 60°, 63.434949°, 68.571429°, 69.930678°, 77.142857°, 77.454884°, 85.714286°, 85.726225° | 24 → 46 → 88 → 130 → 172 → 214 → 296 → 296 → 296 → 296 → 296 → 338 → 338 → 338 → 380 → 380 → 422 → 422 → 464 → 464 → 506 → 506 |
| 24 | [24-gon ring](https://lukacslacko.github.io/axes/#ring24) | 7.5°, 15°, 22.5°, 30°, 37.5°, 45°, 52.5°, 60°, 67.5°, 75°, 82.5° | 25 → 50 → 98 → 146 → 194 → 242 → 290 → 338 → 386 → 434 → 482 → 530 |
| 24 | [22-gon + poles](https://lukacslacko.github.io/axes/#bipyramid22) | 8.181818°, 16.363636°, 24.545455°, 32.727273°, 40.909091°, 45°, 45.293083°, 46.184261°, 47.709342°, 49.090909°, 49.927657°, 52.919851°, 56.780785°, 57.272727°, 61.602534°, 65.454545°, 67.441268°, 73.636364°, 74.265744°, 81.818182°, 81.90035° | 25 → 48 → 92 → 136 → 180 → 224 → 310 → 310 → 310 → 310 → 354 → 354 → 354 → 354 → 398 → 398 → 442 → 442 → 486 → 486 → 530 → 530 |

Each pair tangency is at half the angle between its rays. Every consistent triple of circle equations contributes its sphere-incidence angle; duplicate events are merged. Higher-order coincidences are already among these triple events. These events exhaust the changes of a finite equal-radius small-circle arrangement away from the 0° and 90° endpoints. Each open interval is represented by its midpoint in angle, with every critical value also rendered separately.

For a generic angle, `F = 2p + c + 1`, where `p` is the number of intersecting pairs of circles and `c` is the number of components of their intersection graph, including isolated circles. At critical angles the complete incidence graph is used in `F = E - V + C + 1`; the formula does not treat a multiple intersection as several distinct vertices.

Equal piece counts on either side of an event do not imply the same puzzle. Triple incidences can change which cones contain a sector while preserving the total number of sectors. Orientation, incidence, and connected components are retained by the calculation.

The 90° endpoint adds the opposite rays and deduplicates their planes. Some endpoints therefore exceed the catalogue's directed-axis bound; their cards state the full count. They are useful limits of the displayed families, not extra claims of configurations within the bound.

See [the original model and derivation](model.md) and [the reachability calculation](reachability.md) for the angular sector model, legal turns, and numerical limitations.

## Additional local constructions

These examples are outside the finite global-rule enumeration. Their cut depths are fully drawn, while marked colors remain conservative.

| Rays | Configuration | Critical half-angles | Piece counts in successive open regimes |
|---:|---|---|---|
| 8 | [Gyrobifastigium vertices](https://lukacslacko.github.io/axes/#gyrobifastigium) | 30°, 34.647594°, 45°, 46.550524°, 55.352406°, 56.789089°, 65.65713°, 69.295189°, 70.713675°, 76.102114° | 9 → 11 → 22 → 30 → 30 → 46 → 46 → 46 → 54 → 54 → 54 |
| 24 | [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola) | 20.94102°, 24.374417°, 30.361193°, 41.330505°, 41.882041°, 43.313857°, 48.669495°, 49.911268°, 50.635326°, 53.394417°, 59.638807°, 60.120981°, 60.722387°, 62.161922°, 63.186216°, 63.774708°, 64.542003°, 65.019516°, 65.961365°, 66.556145°, 69.05898°, 69.427116°, 70.35484°, 72.087958°, 73.511774°, 75.404795°, 75.963757°, 77.901715°, 78.847144°, 79.056078°, 79.314273°, 79.921933°, 80.545977°, 82.661009°, 85.096804°, 85.190507°, 85.577721°, 86.203858°, 86.792346°, 87.517969°, 88.346215°, 88.509026° | 25 → 98 → 98 → 170 → 266 → 266 → 266 → 362 → 362 → 362 → 362 → 426 → 426 → 426 → 442 → 442 → 442 → 442 → 442 → 442 → 442 → 522 → 522 → 522 → 522 → 522 → 522 → 522 → 522 → 538 → 538 → 538 → 538 → 538 → 538 → 538 → 538 → 538 → 538 → 538 → 538 → 538 → 538 |
| 3 | [Jumbling example (60° apart)](https://lukacslacko.github.io/axes/#jumble) | 30°, 35.26439° | 4 → 8 → 8 |

## Reachability frontier

The axis configurations and initial cut-arrangement regimes are fully enumerated. Further orbit mergers remain unresolved in these explicitly marked cases:

| Configuration | Displayed angle | Bounds on class count |
|---|---:|---:|
| [8-gon + poles](https://lukacslacko.github.io/axes/#bipyramid8-3) | 51.0007° | 7–14 |
| [8-gon + poles](https://lukacslacko.github.io/axes/#bipyramid8-5) | 68.27949° | 8–10 |
| [8-gon + poles](https://lukacslacko.github.io/axes/#bipyramid8-6) | 79.52949° | 8–9 |
| [8-gon + poles](https://lukacslacko.github.io/axes/#bipyramid8-11) | 67.5° | 7–8 |
| [8-gon + poles](https://lukacslacko.github.io/axes/#bipyramid8-12) | 69.05898° | 7–8 |
| [Tetrahedron + octahedron](https://lukacslacko.github.io/axes/#tetra_octa-4) | 58.683903° | 6–11 |
| [Tetrahedron + octahedron](https://lukacslacko.github.io/axes/#tetra_octa-5) | 63.033572° | 9–14 |
| [Tetrahedron + octahedron](https://lukacslacko.github.io/axes/#tetra_octa-12) | 54.73561° | 4–9 |
| [Tetrahedron + octahedron](https://lukacslacko.github.io/axes/#tetra_octa-13) | 62.632195° | 7–13 |
| [12-gon + poles](https://lukacslacko.github.io/axes/#bipyramid12-3) | 45.496486° | ≤ 44 |
| [12-gon + poles](https://lukacslacko.github.io/axes/#bipyramid12-4) | 47.549789° | ≤ 21 |
| [12-gon + poles](https://lukacslacko.github.io/axes/#bipyramid12-5) | 51.921108° | ≤ 10 |
| [12-gon + poles](https://lukacslacko.github.io/axes/#bipyramid12-6) | 57.367805° | ≤ 9 |
| [12-gon + poles](https://lukacslacko.github.io/axes/#bipyramid12-7) | 61.717474° | ≤ 11 |
| [12-gon + poles](https://lukacslacko.github.io/axes/#bipyramid12-8) | 69.217474° | ≤ 10 |
| [12-gon + poles](https://lukacslacko.github.io/axes/#bipyramid12-9) | 75.244591° | ≤ 12 |
| [12-gon + poles](https://lukacslacko.github.io/axes/#bipyramid12-10) | 82.744591° | ≤ 11 |
| [12-gon + poles](https://lukacslacko.github.io/axes/#bipyramid12-14) | 45.992973° | ≤ 20 |
| [12-gon + poles](https://lukacslacko.github.io/axes/#bipyramid12-15) | 49.106605° | ≤ 9 |
| [12-gon + poles](https://lukacslacko.github.io/axes/#bipyramid12-16) | 54.73561° | ≤ 8 |
| [12-gon + poles](https://lukacslacko.github.io/axes/#bipyramid12-17) | 60° | ≤ 9 |
| [12-gon + poles](https://lukacslacko.github.io/axes/#bipyramid12-18) | 63.434949° | ≤ 9 |
| [12-gon + poles](https://lukacslacko.github.io/axes/#bipyramid12-19) | 75° | ≤ 11 |
| [12-gon + poles](https://lukacslacko.github.io/axes/#bipyramid12-20) | 75.489181° | ≤ 10 |
| [12-gon + poles](https://lukacslacko.github.io/axes/#bipyramid12-21) | 90° | ≤ 1 |
| [16-gon + poles](https://lukacslacko.github.io/axes/#bipyramid16-4) | 45.277892° | ≤ 58 |
| [16-gon + poles](https://lukacslacko.github.io/axes/#bipyramid16-5) | 46.410787° | ≤ 27 |
| [16-gon + poles](https://lukacslacko.github.io/axes/#bipyramid16-6) | 48.761648° | ≤ 12 |
| [16-gon + poles](https://lukacslacko.github.io/axes/#bipyramid16-7) | 52.496558° | ≤ 11 |
| [16-gon + poles](https://lukacslacko.github.io/axes/#bipyramid16-8) | 55.492805° | ≤ 10 |
| [16-gon + poles](https://lukacslacko.github.io/axes/#bipyramid16-9) | 58.597377° | ≤ 12 |
| [16-gon + poles](https://lukacslacko.github.io/axes/#bipyramid16-10) | 64.222377° | ≤ 11 |
| [16-gon + poles](https://lukacslacko.github.io/axes/#bipyramid16-11) | 68.27949° | ≤ 13 |
| [16-gon + poles](https://lukacslacko.github.io/axes/#bipyramid16-12) | 73.90449° | ≤ 12 |
| [16-gon + poles](https://lukacslacko.github.io/axes/#bipyramid16-13) | 78.855403° | ≤ 14 |
| [16-gon + poles](https://lukacslacko.github.io/axes/#bipyramid16-14) | 84.480403° | ≤ 13 |
| [16-gon + poles](https://lukacslacko.github.io/axes/#bipyramid16-19) | 45.555784° | ≤ 26 |
| [16-gon + poles](https://lukacslacko.github.io/axes/#bipyramid16-20) | 47.26579° | ≤ 11 |
| [16-gon + poles](https://lukacslacko.github.io/axes/#bipyramid16-21) | 50.257506° | ≤ 10 |
| [16-gon + poles](https://lukacslacko.github.io/axes/#bipyramid16-22) | 54.73561° | ≤ 9 |
| [16-gon + poles](https://lukacslacko.github.io/axes/#bipyramid16-23) | 56.25° | ≤ 11 |
| [16-gon + poles](https://lukacslacko.github.io/axes/#bipyramid16-24) | 60.944753° | ≤ 10 |
| [16-gon + poles](https://lukacslacko.github.io/axes/#bipyramid16-25) | 67.5° | ≤ 11 |
| [16-gon + poles](https://lukacslacko.github.io/axes/#bipyramid16-26) | 69.05898° | ≤ 11 |
| [16-gon + poles](https://lukacslacko.github.io/axes/#bipyramid16-27) | 78.75° | ≤ 13 |
| [16-gon + poles](https://lukacslacko.github.io/axes/#bipyramid16-28) | 78.960806° | ≤ 12 |
| [16-gon + poles](https://lukacslacko.github.io/axes/#bipyramid16-29) | 90° | ≤ 1 |
| [Cube face + edge axes](https://lukacslacko.github.io/axes/#octa_edges-2) | 30.180597° | ≤ 55 |
| [Cube face + edge axes](https://lukacslacko.github.io/axes/#octa_edges-3) | 32.812792° | ≤ 32 |
| [Cube face + edge axes](https://lukacslacko.github.io/axes/#octa_edges-4) | 40.132195° | ≤ 25 |
| [Cube face + edge axes](https://lukacslacko.github.io/axes/#octa_edges-5) | 46.132895° | ≤ 27 |
| [Cube face + edge axes](https://lukacslacko.github.io/axes/#octa_edges-6) | 51.0007° | ≤ 10 |
| [Cube face + edge axes](https://lukacslacko.github.io/axes/#octa_edges-7) | 57.367805° | ≤ 10 |
| [Cube face + edge axes](https://lukacslacko.github.io/axes/#octa_edges-8) | 60.962223° | ≤ 12 |
| [Cube face + edge axes](https://lukacslacko.github.io/axes/#octa_edges-9) | 63.342522° | ≤ 12 |
| [Cube face + edge axes](https://lukacslacko.github.io/axes/#octa_edges-10) | 66.130299° | ≤ 12 |
| [Cube face + edge axes](https://lukacslacko.github.io/axes/#octa_edges-11) | 67.646173° | ≤ 14 |
| [Cube face + edge axes](https://lukacslacko.github.io/axes/#octa_edges-12) | 68.425663° | ≤ 14 |
| [Cube face + edge axes](https://lukacslacko.github.io/axes/#octa_edges-13) | 70.312015° | ≤ 14 |
| [Cube face + edge axes](https://lukacslacko.github.io/axes/#octa_edges-14) | 72.620051° | ≤ 14 |
| [Cube face + edge axes](https://lukacslacko.github.io/axes/#octa_edges-15) | 75.60807° | ≤ 14 |
| [Cube face + edge axes](https://lukacslacko.github.io/axes/#octa_edges-16) | 83.770545° | ≤ 14 |
| [Cube face + edge axes](https://lukacslacko.github.io/axes/#octa_edges-19) | 30.361193° | ≤ 31 |
| [Cube face + edge axes](https://lukacslacko.github.io/axes/#octa_edges-20) | 35.26439° | ≤ 24 |
| [Cube face + edge axes](https://lukacslacko.github.io/axes/#octa_edges-21) | 45° | ≤ 23 |
| [Cube face + edge axes](https://lukacslacko.github.io/axes/#octa_edges-22) | 47.26579° | ≤ 7 |
| [Cube face + edge axes](https://lukacslacko.github.io/axes/#octa_edges-23) | 54.73561° | ≤ 8 |
| [Cube face + edge axes](https://lukacslacko.github.io/axes/#octa_edges-24) | 60° | ≤ 9 |
| [Cube face + edge axes](https://lukacslacko.github.io/axes/#octa_edges-25) | 61.924446° | ≤ 10 |
| [Cube face + edge axes](https://lukacslacko.github.io/axes/#octa_edges-26) | 64.760598° | ≤ 11 |
| [Cube face + edge axes](https://lukacslacko.github.io/axes/#octa_edges-27) | 67.5° | ≤ 13 |
| [Cube face + edge axes](https://lukacslacko.github.io/axes/#octa_edges-28) | 67.792346° | ≤ 12 |
| [Cube face + edge axes](https://lukacslacko.github.io/axes/#octa_edges-29) | 69.05898° | ≤ 11 |
| [Cube face + edge axes](https://lukacslacko.github.io/axes/#octa_edges-30) | 71.565051° | ≤ 13 |
| [Cube face + edge axes](https://lukacslacko.github.io/axes/#octa_edges-31) | 73.67505° | ≤ 13 |
| [Cube face + edge axes](https://lukacslacko.github.io/axes/#octa_edges-32) | 77.54109° | ≤ 12 |
| [Cube face + edge axes](https://lukacslacko.github.io/axes/#octa_edges-33) | 90° | ≤ 2 |
| [Cube vertices + edge axes](https://lukacslacko.github.io/axes/#cube_edges-2) | 31.22154° | ≤ 36 |
| [Cube vertices + edge axes](https://lukacslacko.github.io/axes/#cube_edges-3) | 33.853735° | ≤ 32 |
| [Cube vertices + edge axes](https://lukacslacko.github.io/axes/#cube_edges-4) | 40.132195° | ≤ 26 |
| [Cube vertices + edge axes](https://lukacslacko.github.io/axes/#cube_edges-5) | 45.688984° | ≤ 26 |
| [Cube vertices + edge axes](https://lukacslacko.github.io/axes/#cube_edges-6) | 47.742287° | ≤ 15 |
| [Cube vertices + edge axes](https://lukacslacko.github.io/axes/#cube_edges-7) | 49.937542° | ≤ 12 |
| [Cube vertices + edge axes](https://lukacslacko.github.io/axes/#cube_edges-8) | 52.752045° | ≤ 12 |
| [Cube vertices + edge axes](https://lukacslacko.github.io/axes/#cube_edges-9) | 55.38004° | ≤ 13 |
| [Cube vertices + edge axes](https://lukacslacko.github.io/axes/#cube_edges-10) | 58.012234° | ≤ 13 |
| [Cube vertices + edge axes](https://lukacslacko.github.io/axes/#cube_edges-11) | 61.717474° | ≤ 15 |
| [Cube vertices + edge axes](https://lukacslacko.github.io/axes/#cube_edges-12) | 64.097774° | ≤ 15 |
| [Cube vertices + edge axes](https://lukacslacko.github.io/axes/#cube_edges-13) | 66.750564° | ≤ 15 |
| [Cube vertices + edge axes](https://lukacslacko.github.io/axes/#cube_edges-14) | 69.634654° | ≤ 15 |
| [Cube vertices + edge axes](https://lukacslacko.github.io/axes/#cube_edges-15) | 71.046915° | ≤ 15 |
| [Cube vertices + edge axes](https://lukacslacko.github.io/axes/#cube_edges-16) | 71.966428° | ≤ 15 |
| [Cube vertices + edge axes](https://lukacslacko.github.io/axes/#cube_edges-17) | 72.757979° | ≤ 17 |
| [Cube vertices + edge axes](https://lukacslacko.github.io/axes/#cube_edges-18) | 73.52302° | ≤ 17 |
| [Cube vertices + edge axes](https://lukacslacko.github.io/axes/#cube_edges-19) | 75.904282° | ≤ 17 |
| [Cube vertices + edge axes](https://lukacslacko.github.io/axes/#cube_edges-20) | 79.440412° | ≤ 17 |
| [Cube vertices + edge axes](https://lukacslacko.github.io/axes/#cube_edges-21) | 81.96035° | ≤ 17 |
| [Cube vertices + edge axes](https://lukacslacko.github.io/axes/#cube_edges-22) | 86.475278° | ≤ 17 |
| [Cube vertices + edge axes](https://lukacslacko.github.io/axes/#cube_edges-25) | 32.443079° | ≤ 28 |
| [Cube vertices + edge axes](https://lukacslacko.github.io/axes/#cube_edges-26) | 35.26439° | ≤ 24 |
| [Cube vertices + edge axes](https://lukacslacko.github.io/axes/#cube_edges-27) | 45° | ≤ 22 |
| [Cube vertices + edge axes](https://lukacslacko.github.io/axes/#cube_edges-28) | 46.377969° | ≤ 12 |
| [Cube vertices + edge axes](https://lukacslacko.github.io/axes/#cube_edges-29) | 49.106605° | ≤ 10 |
| [Cube vertices + edge axes](https://lukacslacko.github.io/axes/#cube_edges-30) | 50.76848° | ≤ 11 |
| [Cube vertices + edge axes](https://lukacslacko.github.io/axes/#cube_edges-31) | 54.73561° | ≤ 11 |
| [Cube vertices + edge axes](https://lukacslacko.github.io/axes/#cube_edges-32) | 56.024469° | ≤ 10 |
| [Cube vertices + edge axes](https://lukacslacko.github.io/axes/#cube_edges-33) | 60° | ≤ 11 |
| [Cube vertices + edge axes](https://lukacslacko.github.io/axes/#cube_edges-34) | 63.434949° | ≤ 13 |
| [Cube vertices + edge axes](https://lukacslacko.github.io/axes/#cube_edges-35) | 64.760598° | ≤ 14 |
| [Cube vertices + edge axes](https://lukacslacko.github.io/axes/#cube_edges-36) | 68.740529° | ≤ 13 |
| [Cube vertices + edge axes](https://lukacslacko.github.io/axes/#cube_edges-37) | 70.528779° | ≤ 14 |
| [Cube vertices + edge axes](https://lukacslacko.github.io/axes/#cube_edges-38) | 71.565051° | ≤ 14 |
| [Cube vertices + edge axes](https://lukacslacko.github.io/axes/#cube_edges-39) | 72.367805° | ≤ 16 |
| [Cube vertices + edge axes](https://lukacslacko.github.io/axes/#cube_edges-40) | 73.148154° | ≤ 14 |
| [Cube vertices + edge axes](https://lukacslacko.github.io/axes/#cube_edges-41) | 73.897886° | ≤ 15 |
| [Cube vertices + edge axes](https://lukacslacko.github.io/axes/#cube_edges-42) | 77.910678° | ≤ 14 |
| [Cube vertices + edge axes](https://lukacslacko.github.io/axes/#cube_edges-43) | 80.970145° | ≤ 16 |
| [Cube vertices + edge axes](https://lukacslacko.github.io/axes/#cube_edges-44) | 82.950556° | ≤ 15 |
| [Cube vertices + edge axes](https://lukacslacko.github.io/axes/#cube_edges-45) | 90° | ≤ 3 |
| [Dodecahedral vertices](https://lukacslacko.github.io/axes/#dodeca-2) | 36.320879° | ≤ 54 |
| [Dodecahedral vertices](https://lukacslacko.github.io/axes/#dodeca-3) | 39.593842° | ≤ 24 |
| [Dodecahedral vertices](https://lukacslacko.github.io/axes/#dodeca-4) | 48.272963° | ≤ 5 |
| [Dodecahedral vertices](https://lukacslacko.github.io/axes/#dodeca-5) | 55.765261° | ≤ 7 |
| [Dodecahedral vertices](https://lukacslacko.github.io/axes/#dodeca-6) | 58.79449° | ≤ 7 |
| [Dodecahedral vertices](https://lukacslacko.github.io/axes/#dodeca-7) | 64.944455° | ≤ 7 |
| [Dodecahedral vertices](https://lukacslacko.github.io/axes/#dodeca-8) | 69.811811° | ≤ 8 |
| [Dodecahedral vertices](https://lukacslacko.github.io/axes/#dodeca-9) | 74.858231° | ≤ 8 |
| [Dodecahedral vertices](https://lukacslacko.github.io/axes/#dodeca-10) | 81.866481° | ≤ 8 |
| [Dodecahedral vertices](https://lukacslacko.github.io/axes/#dodeca-11) | 87.27264° | ≤ 8 |
| [Dodecahedral vertices](https://lukacslacko.github.io/axes/#dodeca-14) | 37.377368° | ≤ 22 |
| [Dodecahedral vertices](https://lukacslacko.github.io/axes/#dodeca-15) | 41.810315° | ≤ 4 |
| [Dodecahedral vertices](https://lukacslacko.github.io/axes/#dodeca-16) | 54.73561° | ≤ 4 |
| [Dodecahedral vertices](https://lukacslacko.github.io/axes/#dodeca-17) | 56.794912° | ≤ 6 |
| [Dodecahedral vertices](https://lukacslacko.github.io/axes/#dodeca-18) | 60.794068° | ≤ 6 |
| [Dodecahedral vertices](https://lukacslacko.github.io/axes/#dodeca-19) | 69.094843° | ≤ 7 |
| [Dodecahedral vertices](https://lukacslacko.github.io/axes/#dodeca-20) | 70.528779° | ≤ 4 |
| [Dodecahedral vertices](https://lukacslacko.github.io/axes/#dodeca-21) | 79.187683° | ≤ 6 |
| [Dodecahedral vertices](https://lukacslacko.github.io/axes/#dodeca-22) | 84.54528° | ≤ 7 |
| [Dodecahedral vertices](https://lukacslacko.github.io/axes/#dodeca-23) | 90° | ≤ 3 |
| [20-gon + poles](https://lukacslacko.github.io/axes/#bipyramid20-5) | 45.177442° | ≤ 72 |
| [20-gon + poles](https://lukacslacko.github.io/axes/#bipyramid20-6) | 45.895941° | ≤ 33 |
| [20-gon + poles](https://lukacslacko.github.io/axes/#bipyramid20-7) | 47.367876° | ≤ 14 |
| [20-gon + poles](https://lukacslacko.github.io/axes/#bipyramid20-8) | 49.662653° | ≤ 13 |
| [20-gon + poles](https://lukacslacko.github.io/axes/#bipyramid20-9) | 52.513276° | ≤ 12 |
| [20-gon + poles](https://lukacslacko.github.io/axes/#bipyramid20-10) | 54.367805° | ≤ 14 |
| [20-gon + poles](https://lukacslacko.github.io/axes/#bipyramid20-11) | 57.144613° | ≤ 13 |
| [20-gon + poles](https://lukacslacko.github.io/axes/#bipyramid20-12) | 61.276808° | ≤ 12 |
| [20-gon + poles](https://lukacslacko.github.io/axes/#bipyramid20-13) | 64.291201° | ≤ 14 |
| [20-gon + poles](https://lukacslacko.github.io/axes/#bipyramid20-14) | 68.791201° | ≤ 13 |
| [20-gon + poles](https://lukacslacko.github.io/axes/#bipyramid20-15) | 72.413981° | ≤ 15 |
| [20-gon + poles](https://lukacslacko.github.io/axes/#bipyramid20-16) | 76.913981° | ≤ 14 |
| [20-gon + poles](https://lukacslacko.github.io/axes/#bipyramid20-17) | 81.054512° | ≤ 16 |
| [20-gon + poles](https://lukacslacko.github.io/axes/#bipyramid20-18) | 85.554512° | ≤ 15 |
| [20-gon + poles](https://lukacslacko.github.io/axes/#bipyramid20-24) | 45.354883° | ≤ 32 |
| [20-gon + poles](https://lukacslacko.github.io/axes/#bipyramid20-25) | 46.436999° | ≤ 13 |
| [20-gon + poles](https://lukacslacko.github.io/axes/#bipyramid20-26) | 48.298754° | ≤ 12 |
| [20-gon + poles](https://lukacslacko.github.io/axes/#bipyramid20-27) | 51.026553° | ≤ 11 |
| [20-gon + poles](https://lukacslacko.github.io/axes/#bipyramid20-28) | 54° | ≤ 12 |
| [20-gon + poles](https://lukacslacko.github.io/axes/#bipyramid20-29) | 54.73561° | ≤ 12 |
| [20-gon + poles](https://lukacslacko.github.io/axes/#bipyramid20-30) | 59.553616° | ≤ 11 |
| [20-gon + poles](https://lukacslacko.github.io/axes/#bipyramid20-31) | 63° | ≤ 13 |
| [20-gon + poles](https://lukacslacko.github.io/axes/#bipyramid20-32) | 65.582403° | ≤ 12 |
| [20-gon + poles](https://lukacslacko.github.io/axes/#bipyramid20-33) | 72° | ≤ 13 |
| [20-gon + poles](https://lukacslacko.github.io/axes/#bipyramid20-34) | 72.827962° | ≤ 13 |
| [20-gon + poles](https://lukacslacko.github.io/axes/#bipyramid20-35) | 81° | ≤ 15 |
| [20-gon + poles](https://lukacslacko.github.io/axes/#bipyramid20-36) | 81.109024° | ≤ 14 |
| [20-gon + poles](https://lukacslacko.github.io/axes/#bipyramid20-37) | 90° | ≤ 1 |
| [Gyrobifastigium vertices](https://lukacslacko.github.io/axes/#gyrobifastigium-2) | 39.823797° | ≤ 18 |
| [Gyrobifastigium vertices](https://lukacslacko.github.io/axes/#gyrobifastigium-3) | 45.775262° | ≤ 23 |
| [Gyrobifastigium vertices](https://lukacslacko.github.io/axes/#gyrobifastigium-4) | 50.951465° | ≤ 20 |
| [Gyrobifastigium vertices](https://lukacslacko.github.io/axes/#gyrobifastigium-5) | 56.070747° | ≤ 32 |
| [Gyrobifastigium vertices](https://lukacslacko.github.io/axes/#gyrobifastigium-6) | 61.22311° | ≤ 23 |
| [Gyrobifastigium vertices](https://lukacslacko.github.io/axes/#gyrobifastigium-7) | 67.476159° | ≤ 20 |
| [Gyrobifastigium vertices](https://lukacslacko.github.io/axes/#gyrobifastigium-8) | 70.004432° | ≤ 24 |
| [Gyrobifastigium vertices](https://lukacslacko.github.io/axes/#gyrobifastigium-9) | 73.407894° | ≤ 22 |
| [Gyrobifastigium vertices](https://lukacslacko.github.io/axes/#gyrobifastigium-10) | 83.051057° | ≤ 22 |
| [Gyrobifastigium vertices](https://lukacslacko.github.io/axes/#gyrobifastigium-13) | 45° | ≤ 22 |
| [Gyrobifastigium vertices](https://lukacslacko.github.io/axes/#gyrobifastigium-14) | 46.550524° | ≤ 19 |
| [Gyrobifastigium vertices](https://lukacslacko.github.io/axes/#gyrobifastigium-15) | 55.352406° | ≤ 28 |
| [Gyrobifastigium vertices](https://lukacslacko.github.io/axes/#gyrobifastigium-16) | 56.789089° | ≤ 20 |
| [Gyrobifastigium vertices](https://lukacslacko.github.io/axes/#gyrobifastigium-17) | 65.65713° | ≤ 19 |
| [Gyrobifastigium vertices](https://lukacslacko.github.io/axes/#gyrobifastigium-18) | 69.295189° | ≤ 20 |
| [Gyrobifastigium vertices](https://lukacslacko.github.io/axes/#gyrobifastigium-19) | 70.713675° | ≤ 20 |
| [Gyrobifastigium vertices](https://lukacslacko.github.io/axes/#gyrobifastigium-20) | 76.102114° | ≤ 21 |
| [Gyrobifastigium vertices](https://lukacslacko.github.io/axes/#gyrobifastigium-21) | 90° | ≤ 6 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-1) | 22.657719° | ≤ 98 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-2) | 27.367805° | ≤ 98 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-3) | 35.845849° | ≤ 170 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-4) | 41.606273° | ≤ 266 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-5) | 42.597949° | ≤ 266 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-6) | 45.991676° | ≤ 266 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-7) | 49.290382° | ≤ 362 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-8) | 50.273297° | ≤ 362 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-9) | 52.014871° | ≤ 362 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-10) | 56.516612° | ≤ 362 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-11) | 59.879894° | ≤ 426 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-12) | 60.421684° | ≤ 426 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-13) | 61.442154° | ≤ 426 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-14) | 62.674069° | ≤ 442 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-15) | 63.480462° | ≤ 442 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-16) | 64.158355° | ≤ 442 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-17) | 64.78076° | ≤ 442 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-18) | 65.49044° | ≤ 442 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-19) | 66.258755° | ≤ 442 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-20) | 67.807562° | ≤ 442 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-21) | 69.243048° | ≤ 522 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-22) | 69.890978° | ≤ 522 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-23) | 71.221399° | ≤ 522 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-24) | 72.799866° | ≤ 522 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-25) | 74.458285° | ≤ 522 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-26) | 75.684276° | ≤ 522 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-27) | 76.932736° | ≤ 522 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-28) | 78.37443° | ≤ 522 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-29) | 78.951611° | ≤ 538 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-30) | 79.185175° | ≤ 538 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-31) | 79.618103° | ≤ 538 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-32) | 80.233955° | ≤ 538 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-33) | 81.603493° | ≤ 538 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-34) | 83.878906° | ≤ 538 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-35) | 85.143656° | ≤ 538 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-36) | 85.384114° | ≤ 538 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-37) | 85.890789° | ≤ 538 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-38) | 86.498102° | ≤ 538 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-39) | 87.155157° | ≤ 538 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-40) | 87.932092° | ≤ 538 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-41) | 88.427621° | ≤ 538 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-42) | 89.254513° | ≤ 538 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-44) | 24.374417° | ≤ 90 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-45) | 30.361193° | ≤ 80 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-46) | 41.330505° | ≤ 218 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-47) | 41.882041° | ≤ 194 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-48) | 43.313857° | ≤ 242 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-49) | 48.669495° | ≤ 242 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-50) | 49.911268° | ≤ 314 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-51) | 50.635326° | ≤ 338 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-52) | 53.394417° | ≤ 314 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-53) | 59.638807° | ≤ 394 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-54) | 60.120981° | ≤ 282 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-55) | 60.722387° | ≤ 402 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-56) | 62.161922° | ≤ 434 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-57) | 63.186216° | ≤ 426 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-58) | 63.774708° | ≤ 426 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-59) | 64.542003° | ≤ 434 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-60) | 65.019516° | ≤ 426 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-61) | 65.961365° | ≤ 426 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-62) | 66.556145° | ≤ 418 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-63) | 69.05898° | ≤ 336 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-64) | 69.427116° | ≤ 474 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-65) | 70.35484° | ≤ 474 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-66) | 72.087958° | ≤ 498 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-67) | 73.511774° | ≤ 490 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-68) | 75.404795° | ≤ 506 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-69) | 75.963757° | ≤ 394 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-70) | 77.901715° | ≤ 506 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-71) | 78.847144° | ≤ 530 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-72) | 79.056078° | ≤ 522 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-73) | 79.314273° | ≤ 522 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-74) | 79.921933° | ≤ 514 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-75) | 80.545977° | ≤ 522 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-76) | 82.661009° | ≤ 402 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-77) | 85.096804° | ≤ 530 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-78) | 85.190507° | ≤ 522 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-79) | 85.577721° | ≤ 522 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-80) | 86.203858° | ≤ 530 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-81) | 86.792346° | ≤ 506 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-82) | 87.517969° | ≤ 522 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-83) | 88.346215° | ≤ 522 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-84) | 88.509026° | ≤ 522 |
| [Elongated square gyrobicupola vertices](https://lukacslacko.github.io/axes/#gyrobicupola-85) | 90° | ≤ 242 |

Shared colors in these cases are established by legal sequences; different colors may still merge. New partial-turn cases intentionally use ordinary generators without an exhaustive search. Earlier verified state-search results are retained. The remaining cases have completed numerical reachability calculations at the displayed angles. Move-state thresholds can further subdivide initial arrangement intervals. See [the reachability methods](reachability.md).
