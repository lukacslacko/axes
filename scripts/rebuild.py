"""Rebuild from the repository root; no network access is needed."""
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parent.parent
(root / 'work').mkdir(exist_ok=True)
import json
limit=max(len(f['axes']) for f in json.loads((root/'data/configurations.json').read_text()) if f.get('scope','global')=='global')
subprocess.run([sys.executable,str(root/'scripts/extend.py'),'--max-axes',str(limit)],cwd=root,check=True)
for name in ['build_site.py', 'previews.py', 'catalogue_docs.py', 'validate.py']:
    print('\n' + name, flush=True)
    subprocess.run([sys.executable, str(root / 'scripts' / name)],
                   cwd=root, check=True)
if limit>=20:subprocess.run([sys.executable,str(root/'scripts/standard_examples.py')],cwd=root,check=True)
import shutil
if shutil.which('node'):subprocess.run(['node',str(root/'scripts/check_renderer.mjs')],cwd=root,check=True)
