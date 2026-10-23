"""Dependency-free static checks; does not claim GPU/scientific validation."""
import ast
import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
for path in sorted((root/'notebooks').glob('*.ipynb')):
    notebook=json.loads(path.read_text())
    assert notebook['cells'], (path, 'empty notebook')
    assert notebook['nbformat']==4
    for index,cell in enumerate(notebook['cells']):
        if cell['cell_type']=='code':
            assert not cell.get('outputs'), (path,index,'clear outputs')
            assert cell.get('execution_count') is None
            ast.parse(''.join(cell['source']),filename=f'{path.name}:cell{index}')
    text=path.read_text()
    for forbidden in ('/Users/', '/home/', 'Bearer as_', 'ghp_'):
        assert forbidden not in text,(path,forbidden)
    assert len({c.get('id') for c in notebook['cells']}) == len(notebook['cells']), (path, 'unique cell IDs required')
    print('PASS',path.name,len(notebook['cells']),'cells')
