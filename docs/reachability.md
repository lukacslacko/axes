# What the colors mean

Each color is a **piece-position reachability class** at the displayed cone half-angle. A move must transport the entire spherical sector into the target sector, with all cut boundaries fitting. Rotations are tracked as three-dimensional matrices, not as a change in a piece's cap-membership bitmask. Disconnected sectors are separate pieces.

The outer body may have arbitrary radial markings or an asymmetric radial profile. A color does not forget a piece's identity or orientation: it describes which angular slots the piece can occupy. Matching colors alone do not solve the asymmetrically marked puzzle. Nor does an orbit imply that every permutation of its pieces is possible.

## Legal moves

For fixed directed axes `u_i` and `h = cos(alpha)`, a turn about `u_i` is legal if every currently placed piece is entirely inside `u_i · x >= h` or entirely outside `u_i · x <= h`. Rotate all pieces on the inside by the same angle. A piece that straddles the cut blocks that axis. Tangencies at boundaries are allowed; pieces of zero area are omitted.

At 90 degrees, add opposite directed rays. These are complementary turns of the same planes. The data and renderer count these additional rays explicitly.

## Standard configurations

For each axis, find its rotation symmetry on the intersecting neighbor axes. Apply the smallest positive such rotation to the pieces in its cap. This gives a permutation of the connected sectors. The orbits of the generated permutations give the colors. A cap with no intersecting neighbors only rotates its own piece in place.

Every possible nonzero alignment of one cut normal with another about a standard axis preserves the whole configuration (using signed normals at 90 degrees). Thus there is no extra interacting-axis switch angle to add to these generators. A noninteracting turn may have arbitrary angle, but cannot carry its piece to another slot.

The reason normal alignment matters: to switch between two intersecting cuts, an open arc of the second cut inside the first cap must be a boundary between rotated pieces. A rotation must therefore carry an existing cut circle to that second cut circle. Returning a piece to an original sector likewise requires its boundary circles to match. Between these angles, a turn can be reversed but creates no additional sector-position equivalence.

The validation checks all moved sectors in both directions, not only their representative points. There are 1,876 cut-normal alignment candidates in the standard configurations including their central limits; all preserve the applicable axis configuration.

## Jumbling example

The three rays have pairwise angle 60 degrees. The partial-turn angle is `acos(1/3) ≈ 70.528779°`. A partial turn can align one neighboring cut while displacing another. Legal next axes therefore depend on the current state.

The search stores a rotation matrix for every physical piece. To test an axis, it evaluates the minimum and maximum of `q · x` on every boundary arc of every piece in its current orientation, plus possible interior extrema at `±q`. Each boundary arc is a sinusoid in its small-circle parameter, so these extrema are evaluated analytically rather than estimated from a mesh. No pieces are allowed to straddle the proposed cut.

Candidate angles align a current moving boundary normal with a fixed cut normal at the same latitude around the turn axis. These are the possible interacting-axis switch angles and slot-fitting angles. Candidate turns that block all other axes are retained too; the search can reverse them. At 90 degrees both signs of each plane normal are used.

The results are:

| Displayed half-angle | Pieces | Class sizes |
|---|---:|---|
| 0° | 1 | 1 |
| 15° | 4 | 1, 1, 1, 1 |
| 30° | 5 | 1, 1, 1, 1, 1 |
| 32.632195° | 8 | 3, 1, 1, 1, 1, 1 |
| 35.264390° | 7 | 3, 1, 1, 1, 1 |
| 62.632195° | 8 | 3, 1, 1, 1, 1, 1 |
| 90° | 8 | 3, 3, 1, 1 |

In the shallow and first overlapping cases, the found transfers attain a geometric upper bound: congruence combined with immobile axis centers and stationary pieces. At 62.632195° the switching graph closes after 25 labeled orientation states (maximum shortest-path depth 2); at 90° it closes after 318 states (depth 6). These counts concern switch/slot-alignment states, not all the continuously available intermediate turn angles. Explicit legal move witnesses for the nontrivial classes are included in `assets/atlas.json` and rechecked by `scripts/validate.py`.

This is a **floating-point computation, not an interval-arithmetic or symbolic proof**. Axis directions are stored to ten decimal places; geometry checks use tolerances on the order of `10^-7` to `10^-6`. State matrices are compared to eight decimal places. The geometric formulas are exact, but their evaluation is numerical. The stated graph sizes are reproducible results with those tolerances.

The open intervals on the page classify the *initial cut arrangement*. The jumbling reachability calculation is for the displayed representative angle and the displayed endpoints; it does not prove that the move-state structure stays constant throughout an interval. Further movement thresholds could subdivide it.

## Geometry and rendering

The cut-arrangement region count is checked with `F = E - V + C + 1` on the sphere, accounting for isolated circles, tangencies, coincident central planes, and multiple intersections. Connectivity is sampled on a 2048 × 1024 spherical atlas, with geodesic edge tests to avoid connecting regions across a tangent cut. Tiny raster fragments at unresolved intersection tips are treated as boundary pixels only when the resulting count agrees with the analytic arrangement count.

The viewer computes the cut circles directly from dot products in its shader. The region atlas supplies connected-component identities. Near an atlas boundary, exact cap membership selects a compatible neighboring label. The finite texture resolution is a rendering approximation; it does not replace the whole-arc legality and fitting checks used for the colors. Piece area estimates are numerical.
