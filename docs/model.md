# Original derivation: conical twisty puzzles through seven axes

For the expanded enumeration, see [the current catalogue](catalogue.md).

This is a mathematical catalogue, derived from rotation groups and spherical circle arrangements, rather than from a list of manufactured puzzles.

The complete finite catalogue below uses **global rotational symmetry of the axis set**. A separate local criterion is given, together with a three-axis jumbling construction. The eleven globally symmetric configurations are **not claimed to exhaust the weaker local criterion or all jumbling puzzles**.

## Model and what counts as a piece

An axis is a unit vector \(u_i\), representing a directed ray. With common cone half-angle \(0<\alpha<90^\circ\), its moving cone is

\[
C_i=\{r\omega:r>0,\ \omega\in S^2,\ u_i\cdot\omega>\cos\alpha\}.
\]

The cut is the boundary of this cone. Its intersection with the unit sphere is the small circle \(u_i\cdot\omega=\cos\alpha\). Thus all combinatorial information is in an arrangement of circles on the sphere. A geometric piece is the radial sector over a **connected** region of the arrangement. Regions with the same inside/outside signature can be disconnected and must not automatically be counted as a single piece.

For the generic asymmetric body, take any generic positive radial function \(\rho(\omega)\), and truncate each radial sector at \(r=\rho(\omega)\). This models a star-shaped asymmetric body. Each sector retains its individual shape and orientation; a solution must return every sector to its original position and orientation. We do not quotient out the symmetries of an unmarked spherical sector. The classification ignores retention hardware and the common apex. Counts below are connected angular regions before adding a mechanism; stationary regions could be joined by a core in a physical design.

Cone moves preserve their angular support. Consequently an asymmetric radial outline can change shape during a turn without introducing collisions with pieces outside the turning cone. This is one reason conical cuts are convenient for an axis-based mathematical model.

## Exact local symmetry

Write \(\theta_{ij}=\arccos(u_i\cdot u_j)\). For equal half-angles below 90 degrees, the relevant neighbors are exactly

\[
N_i(\alpha)=\{u_j:j\ne i,\ \theta_{ij}<2\alpha\}.
\]

These are the other cut circles with a nonempty arc inside the moving cap. Equality is a tangency and is treated separately.

If a nonidentity rotation \(R_i\) about \(u_i\) satisfies

\[
R_iN_i(\alpha)=N_i(\alpha),
\]

then it preserves the entire cut arrangement inside that cone. Outside the cone nothing moves. The resulting piece map therefore permutes the connected angular regions, and all original cuts are available again. This is a sufficient, exact criterion for a repeatable, non-blocking move. It captures the proposed notion of local neighbors without replacing geometric symmetry by mere graph symmetry.

For different cone half-angles, the actual cut arcs and their angles must be preserved. Permuting just an unweighted neighbor graph is not enough.

The local rule alone does not produce a finite list of axis geometries. For example, sufficiently shallow disjoint cones allow arbitrary axis positions. Those cases can be identified combinatorially as trivial, but the interacting jumbling family below shows that continuous geometric parameters also matter for nontrivial examples.

## Complete classification under the global rule

Impose the stronger condition that every axis admits a nonidentity rotation preserving the **entire** axis set:

\[
\forall u_i\in A\quad\exists R_i\ne I:
\quad R_iu_i=u_i,\qquad R_iA=A.
\]

Up to a common spatial rotation, the following are all possibilities for \(1\le |A|\le7\).

| Rays | Configuration | Maximal basic symmetry turns |
|---:|---|---|
| 1 | One ray | Arbitrary, isolated rotation |
| 2 | Antipodal pair | Independent isolated rotations |
| 3 | Regular triangle on a great circle | 180° |
| 4 | Regular square on a great circle | 180° |
| 4 | Regular tetrahedral vertices | 120° |
| 5 | Regular pentagon on a great circle | 180° |
| 5 | Equatorial triangle and both poles | 180° at equator; 120° at poles |
| 6 | Regular hexagon on a great circle | 180° |
| 6 | Octahedral vertices, \(\pm e_x,\pm e_y,\pm e_z\) | 90° |
| 7 | Regular heptagon on a great circle | 180° |
| 7 | Equatorial pentagon and both poles | 180° at equator; 72° at poles |

The directions, not the outside shape, define the polygon/polyhedron names. A great-circle ring is not a planar physical puzzle: its cones and sectors occupy three-dimensional space.

Turn orders are part of a puzzle's specification. Choosing only half-turns on the octahedral set gives a restriction of the quarter-turn puzzle. At depths where some cones are disjoint, isolated rotations are an additional trivial freedom.

### Exhaustiveness proof

For a non-collinear finite set of rays, its rotation symmetry group \(G\) is finite: its action on the rays is faithful and embeds it into a finite permutation group. The global rule says that every chosen ray has nontrivial stabilizer in \(G\), so it must be a pole of a rotation in \(G\).

The finite rotation groups in three dimensions are cyclic, dihedral, tetrahedral, octahedral, and icosahedral. Their pole orbits give the enumeration:

- A cyclic group supplies only its two polar rays.
- A dihedral group supplies a polar pair and two equatorial regular polygons. Combining the two equatorial orbits simply gives a larger regular polygon. With at most seven rays, this yields the rings and the rings with both poles listed above. The small dihedral degeneracies give the square and octahedral cases already included.
- Tetrahedral pole orbits have sizes 4, 4, and 6. These give a tetrahedron or the six octahedral directions; unions exceed seven.
- Octahedral pole orbits have sizes 6, 8, and 12. Only the six-ray orbit fits.
- Icosahedral pole orbits have sizes 12, 20, and 30, so none fits.

The one-ray and antipodal two-ray cases have continuous axial symmetry and are handled separately.

This uses the standard [classification of finite subgroups of SO(3)](https://math.uchicago.edu/~may/REU2020/REUPapers/Bui%2CAn.pdf). The eleven-case enumeration is the small-orbit calculation above.

## Common-depth regimes

Each row lists the critical cone half-angles, in increasing order. They divide \((0,90^\circ)\) into open intervals. The final column lists connected spherical-region counts on those intervals in the same order. Critical angles themselves are degenerate arrangements and should be recorded separately.

| Rays and configuration | Critical half-angles | Regions, shallow to deep |
|---|---|---|
| 1, single ray | None | 2 |
| 2, antipodal pair | None | 3 |
| 3, equatorial triangle | 60° | 4 → 8 |
| 4, equatorial square | 45° | 5 → 10 |
| 4, tetrahedron | 54.735610°, 70.528779° | 5 → 14 → 14 |
| 5, equatorial pentagon | 36°, 72° | 6 → 12 → 22 |
| 5, triangle plus poles | 45°, 60°, 63.434949° | 6 → 14 → 20 → 20 |
| 6, equatorial hexagon | 30°, 60° | 7 → 14 → 26 |
| 6, octahedron | 45°, 54.735610° | 7 → 26 → 26 |
| 7, equatorial heptagon | 180°/7, 360°/7, 540°/7 | 8 → 16 → 30 → 44 |
| 7, pentagon plus poles | 36°, 45°, 51.026553°, 72°, 72.827962° | 8 → 14 → 32 → 32 → 42 → 42 |

There are **32 open common-depth regimes across the eleven axis configurations**. This is a count of the listed arrangement regimes, not a claim of 32 pairwise non-isomorphic abstract puzzle groups. It also excludes the singular transition angles and the 0°/90° endpoints.

Repeated region counts still mark real changes. For tetrahedral axes:

- Below 54.735610°: four independent moving caps and one stationary region.
- Between 54.735610° and 70.528779°: four single-axis regions, six two-axis regions, and four stationary regions.
- Above 70.528779°: four single-axis regions, six two-axis regions, and four three-axis regions.

Thus the final transition replaces four stationary sectors with four sectors affected by three axes, although the total remains fourteen.

### Exact formulas for the transitions

For a ring of \(m\) equatorial rays, pair tangencies occur at

\[
\alpha_k=\frac{k\pi}{m},\qquad k=1,\ldots,\left\lfloor\frac{m-1}{2}\right\rfloor.
\]

No three of its small circles meet at a common point for \(0<\alpha<90^\circ\).

For that ring plus both poles, also include

\[
45^\circ,
\qquad \beta_k=\arctan\!\left(\frac{1}{\cos(k\pi/m)}\right).
\]

The \(\beta_k\) are triple-circle coincidences: two equatorial cuts and a polar cut. For the tetrahedron the two values are

\[
\arccos(1/\sqrt3),\qquad \arccos(1/3).
\]

More generally, a pair first meets at \(\theta_{ij}/2\). For three linearly independent normals, form their Gram matrix \(G=(u_i\cdot u_j)\). A triple point reaches the unit sphere when

\[
\cos\alpha=\frac{1}{\sqrt{\mathbf1^T G^{-1}\mathbf1}}.
\]

This follows by solving the three equations \(u_i\cdot x=\cos\alpha\) and imposing \(\|x\|=1\). Dependent triples require checking consistency separately. There are no additional positive-depth multiple coincidences in these eleven families beyond the listed events.

For generic depths, if \(p\) pairs of cut circles intersect and the intersection graph of circles has \(c\) connected components (including isolated circles), Euler's formula gives

\[
F=2p+c+1.
\]

This verifies the region counts. Triple coincidences can change region membership and adjacency without changing the number of pair intersections on the two sides of the event.

### Unequal cone angles

One cut per axis does not imply a common angle. The table deliberately takes the common-angle slice. If angles vary independently, the result is a chamber decomposition of angle-parameter space, not a single ordered list.

For example, the ring and poles of a triangular or pentagonal bipyramid can have different common angles while preserving the listed global moves. For three independent normals and \(d=(\cos\alpha_i)\), the triple-incidence wall is

\[
d^T G^{-1}d=1.
\]

Pair tangencies and dependent or higher-order circle coincidences must also be included. These walls give an explicit route to an expanded catalogue; it is not included in the 32-regime count.

## The 90-degree endpoint and directed-ray counting

At \(\alpha=90^\circ\), a cone boundary becomes a plane through the origin. Its two sides are equivalent turning halves. With the stated directed-axis convention the full axis set is then \(A\cup(-A)\), and antipodal cuts coincide.

In the globally symmetric catalogue, the distinct central-cut cases that remain within seven rays are:

| Full directed axis set | Distinct central planes | Spherical sectors |
|---|---:|---:|
| Antipodal pair | 1 | 2 |
| Equatorial square | 2 perpendicular planes | 4 |
| Equatorial hexagon | 3 planes through one common line | 6 |
| Octahedral directions | 3 mutually perpendicular planes | 8 |

The tetrahedral four-ray family becomes an eight-ray configuration at the endpoint, exactly as in the question's Skewb convention, and therefore leaves the seven-ray catalogue. The triangular ring's central limit is the same six-ray geometry as the hexagonal ring's central limit. The endpoint must not be treated as an ordinary member of the preceding open interval.

At \(\alpha\to0\), the caps become independent and trivial. At exactly zero the moving cones have no positive angular volume.

## Jumbling and an explicit three-axis family

Lack of global symmetry is not a definition of jumbling. An exact symmetry of each moving cap's local cut arrangement already produces ordinary repeatable moves. Blocking alone can also come from bandaging a finite ordinary puzzle.

A useful formalization is: **intrinsic jumbling occurs when no finite regular subdivision of the pieces makes all relevant interacting switch moves preserve one fixed angular piece partition.** This adapts the conventional definition in terms of inability to unbandage into a doctrinaire puzzle to the present angular model. It deliberately ignores the arbitrary asymmetric exterior, which would otherwise make almost every move look shape-changing. See the original discussion by [Oskar van Deventer and Bram Cohen](https://www.twistypuzzles.com/articles/other-twistypuzzlesthatjumble/).

Here is a construction from geometry alone:

1. Choose three rays with pairwise angle 60°, so \(u_i\cdot u_j=1/2\) for \(i\ne j\).
2. Give each cone half-angle 33°. More generally any angle strictly between 30° and \(\arccos\sqrt{2/3}\approx35.264390^\circ\) works for this simple pair-overlap regime.
3. Turn cone 1 by the angle that carries \(u_2\) to \(u_3\) around \(u_1\).

Projection into the plane perpendicular to \(u_1\) gives

\[
\cos\phi=\frac{u_2\cdot u_3-(u_1\cdot u_2)(u_1\cdot u_3)}
 {\sqrt{1-(u_1\cdot u_2)^2}\sqrt{1-(u_1\cdot u_3)^2}}
=\frac13,
\]

so \(\phi=\arccos(1/3)\approx70.528779^\circ\).

This rotation carries cut 2 exactly onto cut 3 **within cone 1**. Outside cone 1, cut 3 was untouched. Therefore the complete boundary of cone 3 is available and cone 3 can now turn. Cut 2 is blocked. This is a genuine switch between interacting axes, not just a freely spinning isolated cap.

The turn angle is an irrational multiple of \(\pi\). Indeed, if it were a rational multiple, \(2\cos\phi\) would be an algebraic integer; but \(2/3\) is a rational non-integer. A finite regular refinement invariant under this switch would have to accommodate all rotated images of an intersecting cut under repeated rotation by \(\phi\). These are infinitely many distinct cut patches with dense rotational accumulation. They cannot be the boundaries of a finite regular subdivision into positive-interior pieces. Thus the example is intrinsically jumbling under the stated finite-refinement definition.

It has eight connected angular regions at the chosen depth. One is the large exterior region and another is a small stationary gap among the three pairwise-overlapping caps; those two have the same outside-all-caps signature but are disconnected.

This example does **not** satisfy the stricter requirement that a single nonidentity turn permute the whole neighbor set. It illustrates why that requirement is sufficient for ordinary moves but excludes a natural class of jumbling moves. For jumbling one must allow partial seam alignments and state-dependent moves.

Varying the common pairwise dot product to \(c\in(-1/2,1)\) gives

\[
\phi(c)=\arccos\left(\frac{c}{1+c}\right).
\]

One may choose the cone angle between

\[
\frac12\arccos c
\quad\text{and}\quad
\arccos\sqrt{\frac{1+2c}{3}}
\]

to obtain the same pairwise-overlap/no-triple-overlap pattern. Whenever \(\phi(c)/\pi\) is irrational, the same obstruction to finite unbandaging applies. Therefore there is a continuous family of three-axis candidates, with uncountably many intrinsically jumbling members, despite their common initial combinatorial pattern.

The finite eleven-case catalogue, the common-depth regime table, and this broader continuous jumbling family answer different classification questions. Keeping those scopes explicit is essential.
