# New geometry from 13 to 24 axes

The great-circle rings and rings with both poles continue at every size. Four additional polyhedral configurations enter the global-rule catalogue:

| Rays | Construction | Link |
|---:|---|---|
| 14 | Cube vertices together with face-center directions: 8 + 6 | [Gallery](https://lukacslacko.github.io/axes/#octa_cube) |
| 18 | Cube face-center and edge-midpoint directions: 6 + 12 | [Gallery](https://lukacslacko.github.io/axes/#octa_edges) |
| 20 | Cube vertex and edge-midpoint directions: 8 + 12 | [Gallery](https://lukacslacko.github.io/axes/#cube_edges) |
| 20 | Dodecahedral vertices, equivalently icosahedral face-center directions | [Gallery](https://lukacslacko.github.io/axes/#dodeca) |

Each construction is normalized to directed rays; radial distances of the original vertices play no part in the cone arrangement. All rays have the same cut half-angle. The [catalogue](catalogue.md) lists every critical depth and open-regime piece count.

## The extension from 21 to 24 axes

The global rule contributes eight more configurations: a great-circle ring at each of 21, 22, 23, and 24 rays, and a ring of 19, 20, 21, or 22 rays together with both poles. No new tetrahedral, octahedral, or icosahedral pole-orbit union falls in this range; the next is the 26-ray union of all three octahedral pole orbits.

These eight configurations add 129 open arrangement regimes and 266 views including critical depths and endpoints. This brings the global-rule catalogue to 53 configurations and 504 open regimes through 24 rays.

The separate [elongated square gyrobicupola gallery](https://lukacslacko.github.io/axes/#gyrobicupola) adds 43 open regimes, 42 critical depths, and both endpoints. It reaches 538 pieces. It lies outside the global rule and supplies a concrete example of the wider local possibilities. See [its construction and partial-turn witnesses](local-constructions.md). All three local examples together with the global catalogue give 1,178 sphere views.

## An intrinsic-jumbling witness on dodecahedral rays

The presence of an ordinary rotational symmetry about every ray does not preclude additional partial turns. Let `u` be a dodecahedral vertex ray. There are two other vertex rays `a,b` such that

\[
u\cdot a=u\cdot b=\frac13,\qquad a\cdot b=\frac{\sqrt5}{3}.
\]

Explicitly, with `τ = (1+√5)/2`, take

\[
u=(1,1,1)/\sqrt3,\quad a=(1,1,-1)/\sqrt3,\quad
b=(0,\tau,-1/\tau)/\sqrt3.
\]

These are three unit vertex directions of the same regular dodecahedron, so the dot products follow directly from `τ−1/τ = 1` and `τ+1/τ = √5`.

The rotation about `u` carrying `a` to `b` has

\[
\cos\phi=\frac{a\cdot b-(u\cdot a)(u\cdot b)}{1-(u\cdot a)^2}
=\frac{3\sqrt5-1}{8},\qquad \phi\approx44.477512186^\circ.
\]

The two cuts meet the turning cap for `α > ½ acos(1/3) ≈ 35.264390°`. At the illustrative depth **α = 60°**, a turn of this angle leaves six other overlapping axes usable and blocks nine. The coordinate calculation checks a witness on every one of the twenty rays. This 60° example is a move certificate; the gallery continues to use midpoint representatives of its arrangement intervals.

This angle is an irrational multiple of π. If it were rational, `2 cos φ` would be an algebraic integer. But

\[
2\cos\phi=\frac{3\sqrt5-1}{4}
\]

has norm `−11/4` in `Q(√5)`, which is not an integer. Hence the finite-invariant-refinement obstruction from the original [jumbling definition](model.md) applies. This is stronger than merely observing that some axes become blocked.

Run `python3 scripts/standard_examples.py` to reproduce the coordinate checks. The witnesses are stored in `data/standard-examples.json`. This establishes partial-turn behavior, not a complete reachability classification; the new gallery's shared colors remain conservative groups verified by ordinary moves.
