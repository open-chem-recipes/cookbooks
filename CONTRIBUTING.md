# Contributing

Small, independently runnable contributions are welcome. Open an issue before a large recipe so we can agree on scope and compute requirements.

## A recipe should include

1. One concrete task, a small default run and an honest estimate of resources.
2. Public or user-provided data, source links, revisions and split strategy.
3. All task code in the notebook; no private package imports or hosted-service dependency.
4. A baseline and held-out evaluation, alongside training loss.
5. Local results, model/data provenance, seeds and limitations.
6. Failure behavior: missing GPU, invalid inputs, interrupted downloads and insufficient data.

Keep credentials in environment variables. Clear notebook outputs before committing; save selected non-sensitive results in `results/` with a manifest. Do not commit datasets, weights, private run links, personal details or machine-specific paths.

## Before opening a pull request

```bash
python scripts/validate_notebooks.py
python -m unittest discover -s tests
```

Run the recipe in an isolated environment when possible. Include OS, Python, GPU, package versions, elapsed time and any deviations from the default configuration. CI checks notebook structure, syntax and data preparation; GPU training is documented separately in measured results.

Use a focused PR with a short explanation of the problem, change and validation. Report negative results and failed reproductions without changing labels to make the demo look successful.

## Review priorities

Reproducibility, clear evaluation and accessibility matter more than model size. Prefer a useful baseline over a model-name-only showcase. Respect upstream licenses and cite the work that a recipe builds on. Avoid promotional claims or implied affiliations.
