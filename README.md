# Axes

[Explore the atlas](https://lukacslacko.github.io/axes/)

An interactive mathematical catalogue of conical twisty puzzles. All configurations and depths appear on one scrollable page, with jump navigation and an independently rotatable sphere for every case. Pieces share a color when legal turns can carry a whole piece into another piece's angular-sector position.

- **16 standard axis configurations** with at most **9 directed rays**.
- **59 open cut-arrangement regimes**, their critical depths, and both endpoints.
- A three-axis jumbling example, giving **141 sphere views** in total.
- Whole-sector reachability colors, class highlighting, axis labels, and optional piece IDs.
- Mouse/touch rotation, arrow buttons and keyboard controls, and automatic light/dark appearance.

This is a finite catalogue under the **global axis-symmetry rule**, not a classification of every possible locally defined or jumbling puzzle. At the central-cut endpoint, opposite rays can also turn; views that consequently exceed the catalogue’s axis bound are marked. Jumbling reachability is calculated numerically at the displayed angle, not asserted constant over an entire arrangement interval.

See [the current catalogue and completeness argument](docs/catalogue.md), [the mathematical model](docs/model.md) and [the reachability calculation](docs/reachability.md).

## Run locally

No build tools or browser dependencies are required. From this directory:

```sh
python3 -m http.server 8000
```

Open `http://localhost:8000`. Serve over HTTP instead of opening the HTML as a local file. The viewer uses WebGL 2, with a Canvas 2D fallback, and native gzip decompression. All sphere data is served locally; Google Fonts is optional and falls back to system fonts.

Drag to rotate, or focus a sphere and use the arrow keys. `Home` resets its view, `+` / `-` zoom, and `Escape` clears its selected class. Ctrl/Command + wheel zooms; ordinary scrolling keeps moving down the page. On touch devices, vertical swipes scroll the gallery and the arrow buttons provide full rotation.

## Reproduce and validate

The shipped HTML and data are precomputed. Regenerating the geometry needs Python 3, NumPy, and SciPy:

```sh
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python3 scripts/rebuild.py
```

The complete pipeline builds small-circle arrangements, checks region counts with Euler's formula, computes ordinary move permutations, searches state-dependent jumbling moves, generates HTML, and checks every generated whole-sector move image and jumbling witness. Intermediate files go to the ignored `work/` directory.

To validate the shipped data alone:

```sh
python3 scripts/validate.py
node --check app.js
node --check renderer.js
```

The renderer shares **one WebGL context** between every card. Every card has a pre-rendered mathematical preview and its own camera; live canvas buffers are retained only near the viewport, and the decompressed atlas cache is bounded. No third-party rendering library is used.

## License

[MIT](LICENSE), copyright © 2026 László Lukács.
