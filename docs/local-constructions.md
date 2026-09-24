# Beyond global symmetry: the two twisted examples

The finite global-axis enumeration uses a strong condition: **every selected ray is the axis of a nonidentity rotation of the entire ray set**. This is sufficient for ordinary turns at every depth, but it is not necessary for useful conical puzzles. In particular, it excludes both of the vertex sets proposed in the discussion. Direct coordinate calculations nevertheless give interacting, state-dependent moves for both.

The claims below concern the ideal conical sector model. They establish working angular moves and axis switching; they do not supply retention hardware, an exhaustive solution group, or complete piece-equivalence classes for these extra examples.

## A sufficient condition for an axis switch

Start with the original cut arrangement. Let `a` be the turning ray and let `b,c` be other rays satisfying

\[
a\cdot b=a\cdot c,\qquad \angle(a,b)<2\alpha.
\]

A rotation `R` about `a` taking `b` to `c` carries **the entire arc** of cut `b` inside cap `a` onto the entire arc of cut `c` inside that cap. The part of cut `c` outside cap `a` was not moved. Consequently cut `c` is again a complete boundary between pieces, so axis `c` can turn. This argument remains valid when other cuts intersect those arcs.

For any other intersecting axis `d`, its cut remains available after this first turn exactly when a moved boundary-circle normal lands on `d`. Otherwise an open arc of that cut is missing and some piece straddles it. At 90° normals are considered with both signs.

Thus **two neighbors at the same angular distance can suffice for a useful partial turn**. The whole neighbor set need not have a cyclic symmetry. The precise turn angle is

\[
\cos\phi=\frac{b\cdot c-(a\cdot b)(a\cdot c)}
 {\sqrt{1-(a\cdot b)^2}\sqrt{1-(a\cdot c)^2}}.
\]

This condition is sufficient, not a proposed complete classification of all useful moves. After several partial turns, the fixed starting diagram no longer describes all boundary arcs, and legality must be checked in the resulting state.

## Eight rays: gyrobifastigium

Glue two equilateral triangular prisms along a square and turn one prism by 90° relative to the other. Centering the shared square at the origin gives vertices

\[
(\pm\tfrac12,\pm\tfrac12,0),\quad
(0,\pm\tfrac12,\tfrac{\sqrt3}{2}),\quad
(\pm\tfrac12,0,-\tfrac{\sqrt3}{2}).
\]

Normalize each vertex to obtain the eight rays. The square vertices and ridge vertices have different radii before normalization; using their directions is essential.

Take

\[
a=(0,\tfrac12,\tfrac{\sqrt3}{2}),\quad
b=(1,1,0)/\sqrt2,\quad c=(-1,1,0)/\sqrt2.
\]

Then `a·b = a·c = 1/(2√2)` and `b·c = 0`, so

\[
\phi=\arccos(-1/7)=98.213210702^\circ.
\]

Both relevant cuts intersect cap `a` as soon as

\[
\alpha>\tfrac12\arccos(1/(2\sqrt2))=34.647594473^\circ.
\]

At **α = 40°**, the four rays through the shared-square vertices admit ordinary 180° turns. Each of the four ridge rays admits a 98.213° partial turn that opens one intersecting axis and blocks two. Every ray therefore has an interacting use, despite the full set failing the global rule.

The angle is an irrational multiple of π: otherwise `2 cos φ = −2/7` would be an algebraic integer, impossible for a rational noninteger. This provides the same obstruction to a finite invariant refinement discussed in the original model's jumbling section.

### A continuous deformation

Keep the four equatorial rays `(±1,±1,0)/√2`, and replace the ridge rays by

\[
(0,\pm\sin\beta,\cos\beta),\quad
(\pm\sin\beta,0,-\cos\beta),\qquad 0<\beta<90^\circ.
\]

The regular solid is β = 30°. For the corresponding ridge switch,

\[
\cos\phi(\beta)=-\frac{\sin^2\beta}{2-\sin^2\beta},\qquad
\alpha>\tfrac12\arccos(\sin\beta/\sqrt2).
\]

The four equatorial half-turns persist. Hence the useful construction survives a continuous variation of the angular distances; it is not an isolated accident of the regular-faced polyhedron. This also illustrates why a finite list of ray geometries cannot cover the broader local/jumbling interpretation, even at eight rays.

## Twenty-four rays: elongated square gyrobicupola

Let `s = 1+√2`. Begin with the 24 coordinate permutations of `(±s,±1,±1)`. Rotate the four vertices with `z=s` by 45° about the z-axis, then normalize all 24 vertices. This twists one square cupola while its octagonal base maps to itself. The resulting circumspherical geometry agrees with the [24-vertex polyhedral data of David McCooey](https://dmccooey.com/polyhedra/ElongatedSquareGyrobicupola.html).

The squared circumradius before normalization is `5+2√2`, with edge length 2. Each ray therefore has four edge-neighbor rays at angular distance

\[
\theta=\arccos\left(\frac{3+2\sqrt2}{5+2\sqrt2}\right)
=41.882040944^\circ.
\]

Their azimuthal gaps about the vertex ray have one value corresponding to the incident triangle and three equal values corresponding to the squares. The four-neighbor set has no nonidentity cyclic symmetry: equal face-incidence patterns are not the same thing as a rotation around the vertex ray. Once the nearest cuts interact, this rules out a diagram-preserving ordinary turn at every vertex.

Nevertheless, at **α = 25°**, all 24 axes admit interacting partial turns. Choosing the pair of edge-neighbors joined by the triangular face gives

\[
\phi=\arccos\left(\frac{2+\sqrt2}{8}\right)
=64.736825646^\circ.
\]

The first-turn calculation opens one other intersecting axis and blocks three. Thus the twist does not prevent a conical angular mechanism; global or full-neighbor symmetry would simply be too restrictive a criterion to recognize it.

Again this angle is an irrational multiple of π. The algebraic norm of `2 cos φ = (2+√2)/4` is `1/8`, whereas an algebraic integer has integer norm. The finite-refinement obstruction therefore applies here too.

## Reproduction and scope

Run `python3 scripts/local_examples.py`. The script constructs both ray sets, checks each first-turn circle alignment and the opened/blocked axes, and verifies five points in the gyrobifastigium deformation family. Coordinates, move witnesses for every ray, and all initial cut-arrangement critical angles are stored in `data/local-examples.json`.

These two constructions extend the *mathematical investigation*, and the [gyrobifastigium gallery](https://lukacslacko.github.io/axes/#gyrobifastigium) now includes all its initial cut-arrangement depths, with conservative colors backed by ordinary turns. The 24-axis example remains a documented construction. Full state-dependent reachability for these local families is still separate work; the switches above do not settle those harder questions.
