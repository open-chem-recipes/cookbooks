# Open Chem Recipes

<img src="assets/molecules-banner.png" alt="AI-generated illustration of molecular structures" width="100%">

Self-contained notebooks for fine-tuning chemistry and biomolecular models. One model, one recipe: public data, visible training code, held-out evaluation and saved results.

| Model | Recipe | Adaptation | Data |
|---|---|---|---|
| **ChemFM-1B** | [Solubility prediction](notebooks/01_chemfm_solubility.ipynb) | LoRA + regression head | ESOL, scaffold-separated subsets |
| **FAIR-Chem / UMA-S** | [Molecular energies and forces](notebooks/02_uma_energy_forces.ipynb) | Official UMA fine-tuning pipeline | rMD17 ethanol structures |
| **BioEmu-2** | [Protein readout adaptation](notebooks/03_bioemu2_mdcath.ipynb) | 1,152 readout weights | Small public mdCATH subset |

These small defaults demonstrate how to adapt a model. They are not reproductions of published benchmarks or evidence that fine-tuning always improves performance. See [measured results](results/README.md).

## Run a recipe

Use a **separate Python 3.12 environment for each notebook**. Each has its own dependency installation cells. Install Git and a C/C++ compiler first (Debian/Ubuntu: `sudo apt-get install git build-essential`). NVIDIA CUDA is required for the training defaults; memory requirements have only been tested on an H200.

```bash
git clone https://github.com/open-chem-recipes/cookbooks.git
cd cookbooks
python3.12 -m venv .venv-chemfm
source .venv-chemfm/bin/activate
python -m pip install --upgrade pip jupyterlab ipykernel
python -m ipykernel install --user --name chemfm-recipe --display-name 'ChemFM recipe'
jupyter lab
```

Choose the matching kernel and run the cells in order. Repeat with a new environment/kernel for UMA and BioEmu-2.

- **Outputs:** local checkpoints, JSON metrics and plots. No hosted application is required.
- **W&B:** offline by default without credentials. Set `WANDB_API_KEY`, optionally `WANDB_PROJECT` and `WANDB_ENTITY`, for online charts. `WANDB_MODE=offline` explicitly keeps logging local in the ChemFM and UMA recipes.
- **UMA storage:** keep the Python environment and output directory on a persistent disk with at least 30 GiB free. The recipe places model/compiler caches and temporary files there; on Kubernetes, also configure ephemeral-storage requests and limits.
- **UMA access:** request access to [facebook/UMA](https://huggingface.co/facebook/UMA), then use Hugging Face login, `HF_TOKEN` or `HF_TOKEN_FILE`. Never paste tokens into cells or commit them.
- **Reproducibility:** model/data revisions and selected download checksums are pinned. Splits and scaling are explicit. Package versions from measured runs are saved with results.

## Evaluation

**ChemFM:** train-only target scaling; separate scaffold groups for training, validation and test; validation-selected adapters; RMSE/MAE and a training-mean baseline. Its initial regression head is random, not a pretrained solubility predictor.

**UMA:** disjoint original frame IDs, energy/force evaluation before and after adaptation, and energy offsets fitted on training structures only. The molecule is shared across splits, and the source and target levels of theory differ.

**BioEmu-2:** a separate protein for this recipe's evaluation, paired denoising inputs, loss and structure comparison. This is readout adaptation, not full-model training or an equilibrium-ensemble benchmark.

## Contribute

Useful additions include new model recipes, stronger baselines, independent reruns, dataset adapters and dependency fixes. Start with a [recipe proposal](https://github.com/open-chem-recipes/cookbooks/issues/new?template=recipe.yml).

See [contribution guidelines](CONTRIBUTING.md), [code of conduct](CODE_OF_CONDUCT.md), [responsible use](RESPONSIBLE_USE.md), [security](SECURITY.md) and [citation metadata](CITATION.cff).

## Licensing and sources

Original recipe code is MIT licensed. Downloaded weights, datasets and upstream components keep their own terms. See [licenses and attribution](THIRD_PARTY_NOTICES.md); the repository license does not relicense those assets.

- [ChemFM](https://github.com/TheLuoFengLab/ChemFM)
- [FAIR-Chem](https://github.com/facebookresearch/fairchem)
- [BioEmu-2](https://github.com/microsoft/bioemu2)
