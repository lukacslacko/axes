# What the colors mean

Each shared color is backed by **verified piece-position reachability** at the displayed cone half-angle. Marked cases use conservative groups: different colors may still be equivalent. A “≤” class count gives the number of verified groups; a range additionally uses a geometric bound. New partial-turn cases intentionally stop at ordinary generators so the geometry catalogue can expand without an exhaustive orbit search. A move must transport the entire spherical sector into the target sector, with all cut boundaries fitting. Rotations are tracked as three-dimensional matrices, not as a change in a piece's cap-membership bitmask. Disconnected sectors are separate pieces.

The outer body may have arbitrary radial markings or an asymmetric radial profile. A color does not forget a piece's identity or orientation: it describes which angular slots the piece can occupy. Matching colors alone do not solve the asymmetrically marked puzzle. Nor does an orbit imply that every permutation of its pieces is possible.

## Legal moves

For fixed directed axes `u_i` and `h = cos(alpha)`, a turn about `u_i` is legal if every currently placed piece is entirely inside `u_i · x >= h` or entirely outside `u_i · x <= h`. Rotate all pieces on the inside by the same angle. A piece that straddles the cut blocks that axis. Tangencies at boundaries are allowed; pieces of zero area are omitted.

At 90 degrees, add opposite directed rays. These are complementary turns of the same planes. The data and renderer count these additional rays explicitly.

## Standard configurations

For each axis, find its rotation symmetry on the intersecting neighbor axes. Apply the smallest positive such rotation to the pieces in its cap. This gives a permutation of the connected sectors. The orbits of the generated permutations give the colors. A cap with no intersecting neighbors only rotates its own piece in place.

Through nine axes, every possible alignment of one cut normal with another about a standard axis preserves the whole configuration. The first exceptions through twelve axes are: **the octagon plus poles, tetrahedron plus octahedron, and cube-edge configurations admit extra partial turns**. The validator checks normal-alignment candidates for the entire current catalogue; larger configurations introduce more exceptions.

Normal alignment matters because an interacting-axis switch must carry an open arc of an existing boundary circle onto the newly available cut. Noninteracting cap spins change no piece-position classes. Where extra switches exist, ordinary generators alone need not give a complete coloring. New cases with such switches are always marked conservative, even when their groups might already be complete.

### Additional classes from partial turns

The calculation searches legal partial-turn sequences which restore the original piece diagram. Every resulting permutation is checked against the full curved sectors, including all intermediate move legalities. These permutations are then added to the ordinary generators. The published data includes **39 explicit restoring-loop certificates**. For example, some cube-edge cases have four ordinary classes of six that become a single class of 24 when partial turns are allowed.

The search compares *unlabeled geometric diagrams*, while retaining the rotation of each labeled physical piece. If two paths reach the same diagram, the first path followed by the reverse of the second is a candidate restoring loop. Its legality and complete piece permutation are independently checked before it contributes to the colors. Diagram keys retain the oriented supporting circles and boundary-arc endpoints, midpoints, and spans; a geometric hash match by itself is not accepted as a legal transfer certificate.

Two methods establish completeness at a displayed angle:

1. The verified orbit partition reaches an upper bound obtained from whole-sector rotational congruence and immobile pieces. Rotation candidates are derived from supporting-circle normals, then checked on complete arcs in both directions. Congruence is used only as an upper bound, never by itself as proof of reachability.
2. The complete relevant diagram graph closes. The closed graph is also checked for pieces that fit an original slot in a temporarily jumbled diagram, so the calculation does not silently restrict reachability to states where the whole puzzle has returned to its original cut partition.

All computations use floating-point geometry and stated tolerances; these are numerical certificates, not symbolic or interval-arithmetic proofs.

### The earlier nine unresolved searches

Five cases of **the octagon plus poles** and four cases of **tetrahedron plus octahedron** still have gaps between the proven orbit partition and the congruence upper bound. The search generated at least 50,000 distinct diagrams for each, but did not exhaust their graphs or settle every possible merger. The queued frontier is not counted as exhaustively explored. Each such card shows a class-count range: the geometric argument gives the lower count, and verified move sequences give the upper count. The colors display only the established groups.

For the complete list of unresolved angles and bounds, see [the catalogue](catalogue.md#reachability-frontier). No assumption that a long search has proved impossibility is made.

### Blocking versus intrinsic jumbling

The ten-ray tetrahedron–octahedron combination supplies an instructive distinction. Adding the missing opposite tetrahedron gives a 14-ray cut set invariant under the 120° tetrahedral turns and 90° coordinate-axis turns. The original puzzle is therefore a bandaging of a finite regular refinement: it has state-dependent blocking and partial turns, but fails the stronger *intrinsic jumbling* definition in the original model.

The cube-edge partial angle `acos(1/3)` is instead an irrational multiple of π and supplies the finite-refinement obstruction discussed for the original three-axis example. The two user-suggested twisted polyhedra are treated separately in [Local constructions](local-constructions.md).

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

This is a **floating-point computation, not an interval-arithmetic or symbolic proof**. Axis directions are stored to ten decimal places; geometry checks use tolerances on the order of `10^-7` to `10^-6`. State matrices are compared to eight decimal places; extended-diagram feature keys use six decimal places and every proposed loop is subsequently checked geometrically. The geometric formulas are exact, but their evaluation is numerical. The stated graph sizes are reproducible results with those tolerances.

The open intervals on the page classify the *initial cut arrangement*. The jumbling reachability calculation is for the displayed representative angle and the displayed endpoints; it does not prove that the move-state structure stays constant throughout an interval. Further movement thresholds could subdivide it.

## Geometry and rendering

The cut-arrangement region count is checked with `F = E - V + C + 1` on the sphere, accounting for isolated circles, tangencies, coincident central planes, and multiple intersections. Connectivity is sampled on a 2048 × 1024 spherical atlas, refined to 4096 × 2048 where a narrow regime requires it, with geodesic edge tests to avoid connecting regions across a tangent cut. Tiny raster fragments at unresolved intersection tips are treated as boundary pixels only when the resulting count agrees with the analytic arrangement count.

The viewer computes the cut circles directly from dot products in its shader. The region atlas supplies connected-component identities. Near an atlas boundary, exact cap membership selects a compatible neighboring label. The finite texture resolution is a rendering approximation; it does not replace the whole-arc legality and fitting checks used for the colors. Piece area estimates are numerical.

For thin cells, the generator probes both sides of every open boundary arc. When every region has a distinct cap signature, this identifies all components directly. Otherwise it can connect arc probes and raster components by analytically checking that the joining short great-circle path crosses no cut. Every real region has a boundary probe, and connections stay within regions; matching the resulting component count to Euler’s count certifies that no missing or falsely split region remains. A piece can therefore exist in the mathematical data even if it has no interior texel at the displayed resolution.

The viewer loads a small manifest and fetches each sphere on approach to the viewport. Region labels use one or two bytes as needed; fallback maps are sparse in the number of actual pieces rather than exponential in the axis count. The reproducible full dataset remains in `assets/atlas.json`.
