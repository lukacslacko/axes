# Complete global-rule catalogue through 9 axes

The rendered atlas contains **16 standard configurations, 59 open common-angle regimes, and 141 views** including critical depths, endpoints, and the separate jumbling example. Counts refer to directed rays, not unoriented lines. All configurations are derived from finite rotation groups, without consulting a catalogue of manufactured puzzles.

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

Each pair tangency is at half the angle between its rays. Every consistent triple of circle equations contributes its sphere-incidence angle; duplicate events are merged. Higher-order coincidences are already among these triple events. These events exhaust the changes of a finite equal-radius small-circle arrangement away from the 0° and 90° endpoints. Each open interval is represented by its midpoint in angle, with every critical value also rendered separately.

For a generic angle, `F = 2p + c + 1`, where `p` is the number of intersecting pairs of circles and `c` is the number of components of their intersection graph, including isolated circles. At critical angles the complete incidence graph is used in `F = E - V + C + 1`; the formula does not treat a multiple intersection as several distinct vertices.

Equal piece counts on either side of an event do not imply the same puzzle. Triple incidences can change which cones contain a sector while preserving the total number of sectors. Orientation, incidence, and connected components are retained by the calculation.

The 90° endpoint adds the opposite rays and deduplicates their planes. Some endpoints therefore exceed the catalogue's directed-axis bound; their cards state the full count. They are useful limits of the displayed families, not extra claims of configurations within the bound.

See [the original model and derivation](model.md) and [the reachability calculation](reachability.md) for the angular sector model, legal turns, and numerical limitations.
