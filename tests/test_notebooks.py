import json
import hashlib
import tempfile
import unittest
import urllib.request
from pathlib import Path
import numpy as np
import pandas as pd
from rdkit import Chem
from rdkit.Chem.Scaffolds import MurckoScaffold

ROOT=Path(__file__).resolve().parents[1]
class RecipeTests(unittest.TestCase):
    def test_three_model_recipes(self):
        self.assertEqual({p.name for p in (ROOT/'notebooks').glob('*.ipynb')},
                         {'01_chemfm_solubility.ipynb','02_uma_energy_forces.ipynb','03_bioemu2_mdcath.ipynb'})

    def test_chemfm_data_checksum_and_scaffold_split(self):
        notebook=json.loads((ROOT/'notebooks/01_chemfm_solubility.ipynb').read_text())
        source=next(''.join(c['source']) for c in notebook['cells'] if "DATA_REV='455" in ''.join(c['source']))
        with tempfile.TemporaryDirectory() as directory:
            ns={'work':Path(directory),'urllib':__import__('urllib'),'hashlib':hashlib,'pd':pd,'np':np,
                'Chem':Chem,'MurckoScaffold':MurckoScaffold,'json':json,'SEED':42}
            exec(source,ns)
            self.assertEqual([len(ns[k]) for k in ('train','val','test')],[128,32,32])
            self.assertAlmostEqual(ns['mean'],ns['train'].target.mean())
            for a,b in [('train','val'),('train','test'),('val','test')]:
                self.assertFalse(set(ns[a].smiles)&set(ns[b].smiles))
                self.assertFalse(set(ns[a].scaffold)&set(ns[b].scaffold))

    def test_model_and_data_revisions_are_pinned(self):
        for path in (ROOT/'notebooks').glob('*.ipynb'):
            text=path.read_text()
            import re
            self.assertGreaterEqual(len(set(re.findall(r'\b[a-f0-9]{40}\b',text))),2,path.name)

if __name__=='__main__':unittest.main()
