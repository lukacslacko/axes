"""Rebuild from the repository root; no network access is needed."""
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parent.parent
(root / 'work').mkdir(exist_ok=True)
for name in ['build_geometry.py', 'piece_orbits.py', 'extended_orbits.py', 'restore_loops.py', 'switch_graph.py', 'orbit_bounds.py',
             'jumble_orbits.py', 'build_site.py', 'previews.py', 'catalogue_docs.py', 'validate.py']:
    print('\n' + name, flush=True)
    subprocess.run([sys.executable, str(root / 'scripts' / name)],
                   cwd=root, check=True)
