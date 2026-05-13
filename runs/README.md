# Run configuration

`smoke.yaml` caps stochastic budgets for **local smoke** and CI-friendly notebooks. Full archival runs override via env or a `runs/full.yaml` (add when ready) and must log seeds.

`ci_notebooks.yaml` lists notebooks executed headlessly in GitHub Actions after `pytest` (see `scripts/ci_execute_smoke_nb.py`).

On **CI failure**, GitHub Actions uploads `notebooks/`, `runs/`, and `scripts/ci_execute_smoke_nb.py` as a downloadable artifact for debugging.

Optional rows may set `enabled: false` so future charter notebooks stay listed without running in CI until they are stable headless.

**`notebooks/CHARTER_SHELL.ipynb`** (minimal preamble + run card) runs in CI **after** the three `SMOKE_*.ipynb` notebooks (see [`ci_notebooks.yaml`](ci_notebooks.yaml) for order) and **before** `CHARTER_EXTENDED_LIGHT`, **`CHARTER_LAYER_A_MULTIDRAW_SMOKE`**, and the domain stream charter—extend it as the charter grows.

**`notebooks/CHARTER_EXTENDED_LIGHT.ipynb`** (synthetic mean + run card) runs next as a light Layer A–shaped check.

**`notebooks/CHARTER_LAYER_A_MULTIDRAW_SMOKE.ipynb`** — synthetic two-sample pooled-label **permutation** null (Hub-free), capped by `runs/smoke.yaml`; runs **before** the domain stream charter row in [`ci_notebooks.yaml`](ci_notebooks.yaml).

**`notebooks/CHARTER_WIKITEXT_STREAM_SMOKE.ipynb`** runs next: small streaming slice of `Salesforce/wikitext` (`wikitext-2-raw-v1`) + y-shuffle null on log text length + run card (long-text smoke only).

**`FUTURE_CHARTER_SLOT.ipynb`** is listed disabled with **no** committed file: replace that row with a real path when you add a heavier charter notebook, verify headless execution locally, then set `enabled: true`.

## Promotion audit (canonical numbers)

Template: [`runs/promotion_audit.example.yaml`](promotion_audit.example.yaml) — copy the `example_entry` shape when recording a promotion; fill **`commit_sha`** (`github.sha` in Actions, `git rev-parse HEAD` locally) and optional **`ci_run_url`**. Full gate: [meta `PROMOTION_CHECKLIST.md`](https://github.com/SVG-campus/Research/blob/main/docs/PROMOTION_CHECKLIST.md).

## Next validation (honest)

- Prefer trajectory, ephemeris, engineering-telemetry, or mission-scale tabular/streaming datasets for the next heavyweight charter notebook; **`CHARTER_WIKITEXT_STREAM_SMOKE` remains long-text infra smoke**, not evidence for orbital or systems feasibility claims.
- When a domain-native notebook is stable headless locally, **`FUTURE_CHARTER_SLOT`** in [`ci_notebooks.yaml`](ci_notebooks.yaml) should be swapped to that path and **`enabled: true`** only after verifying the notebook runs cleanly in CI.
- Canonical promotion still requires **`runs/promotion_audit.example.yaml`–shaped audit entries**, **`trace_run_ids`** aligned with actual CI **`run_id` strings**, run cards/metric excerpts tied to promoted claims, and the meta gate in [`docs/PROMOTION_CHECKLIST.md`](https://github.com/SVG-campus/Research/blob/main/docs/PROMOTION_CHECKLIST.md).
- Do **not** infer spacecraft, mission, or large-scale systems feasibility from wikitext or other generic NLP smoke; treat those notebooks as scaffolding until domain data pins land.
