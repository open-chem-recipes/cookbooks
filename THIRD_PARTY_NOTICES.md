# Models, datasets and attribution

Checked 2026-10-23. Original recipe code is MIT licensed. Downloaded code, model weights and datasets retain their own terms; this repository does not relicense them or redistribute checkpoints.

| Asset | Declared terms | Source |
|---|---|---|
| ChemFM-1B weights | MIT model-card declaration | [Pinned model card](https://huggingface.co/ChemFM/ChemFM-1B/blob/f99dc2e89726539bb9cf31b2e2b4360650bac6a8/README.md) |
| ChemFM original source repository | CC BY-NC 4.0 | [Upstream source](https://github.com/TheLuoFengLab/ChemFM) |
| ESOL / Delaney data | Retrieved from DeepChem's MIT-licensed repository; original data paper cited below | [Pinned CSV](https://github.com/deepchem/deepchem/blob/455d07f3e17e880a4d980b5b0365e4a02b417e14/datasets/delaney-processed.csv) |
| FAIR-Chem core code | MIT, with third-party notices | [Pinned source](https://github.com/facebookresearch/fairchem/tree/645af7d03e91138ef07e51de387316c9e2e152dc) |
| UMA weights | FAIR Chemistry License v1, including its acceptable-use terms; gated access | [Pinned license](https://huggingface.co/facebook/UMA/blob/c5107e43d5e811dd7cb56f57533dc0eb550dee6b/LICENSE) |
| rMD17 | CC0 dataset release | [Original dataset](https://doi.org/10.6084/m9.figshare.12672038), [pinned NPZ conversion](https://github.com/andersx/rmd17-npz/tree/4f6bb0a186822c90d47cd98b7a27991fe0b3173b) |
| BioEmu-2 code | MIT, with third-party notices | [Pinned source](https://github.com/microsoft/bioemu2/tree/06be369dd555849165a737472d42d936959e46fc) |
| BioEmu-2 weights | MIT | [Pinned model card](https://huggingface.co/microsoft/bioemu2/blob/dd4b0c1b69984b68edcb6200a544213be4d75242/README.md) |
| mdCATH | CC BY 4.0 | [Pinned dataset card](https://huggingface.co/datasets/compsciencelab/mdCATH/blob/5e3ed8aec62b689e01751db16275fdcdbc39e47f/README.md) |

## ChemFM and ESOL

ChemFM: Cai et al., *A Foundation Model for Chemical Design and Property Prediction*, [arXiv:2410.21422](https://arxiv.org/abs/2410.21422). Recipe 01 uses Hugging Face model weights with an independently written PEFT training loop; it does not copy the upstream fine-tuning scripts. The differing source/weight license declarations should not be treated as interchangeable.

ESOL: John S. Delaney, *ESOL: Estimating Aqueous Solubility Directly from Molecular Structure*, Journal of Chemical Information and Computer Sciences (2004), [doi:10.1021/ci034243x](https://doi.org/10.1021/ci034243x). The notebook downloads DeepChem's processed CSV and creates a small scaffold split. The original publication and data provenance remain relevant independently of DeepChem's code license.

## UMA and rMD17

UMA is developed by Meta FAIR. The notebook uses the official FAIR-Chem training pipeline and converts a small ethanol subset to ASE structures, with energy/force units converted to eV and eV/Å. Using or sharing adapted UMA weights remains subject to the UMA license; the MIT recipe license does not override it.

rMD17: Anders S. Christensen and O. Anatole von Lilienfeld, *On the role of gradients for machine learning of molecular energies and forces* (2020), [arXiv:2007.09593](https://arxiv.org/abs/2007.09593). Structures come from MD trajectories and are not guaranteed independent. The recipe uses disjoint frame IDs, but this does not remove temporal correlation or establish generalization to other molecules.

## BioEmu-2 and mdCATH

BioEmu-2 is developed by Microsoft Research. Recipe 03 is an independent readout-adaptation experiment, not an official fine-tuning recipe or evidence of improved equilibrium ensemble sampling.

A. Mirarchi, T. Giorgino and G. De Fabritiis. *mdCATH: A Large-Scale MD Dataset for Data-Driven Computational Biophysics.* Scientific Data 11, 1299 (2024). [Paper](https://doi.org/10.1038/s41597-024-04140-z), [dataset](https://doi.org/10.57967/hf/5055), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

Recipe 03 selects and centers frames from two domains, extracts C-alpha traces and compares paired denoising outputs. The reference trace in `results/03-result.json` and its chart is derived from mdCATH and retains this attribution. Model-generated traces are identified separately. No endorsement by upstream authors is implied.

Dependencies retain their own licenses. Full datasets and model weights are not bundled in this repository.
