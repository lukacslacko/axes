# Complete global-rule catalogue through 20 axes

The rendered atlas contains **45 standard configurations, 375 open common-angle regimes, and 825 views** including critical depths, endpoints, and the two local examples. Counts refer to directed rays, not unoriented lines. All standard configurations are derived from finite rotation groups, without consulting a catalogue of manufactured puzzles.

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

Shared colors in these cases are established by legal sequences; different colors may still merge. New partial-turn cases intentionally use ordinary generators without an exhaustive search. Earlier verified state-search results are retained. The remaining cases have completed numerical reachability calculations at the displayed angles. Move-state thresholds can further subdivide initial arrangement intervals. See [the reachability methods](reachability.md).
