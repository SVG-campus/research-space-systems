# Preregistration — `research-space-systems`
 
**Pillar:** `research-space-systems`  
**Title:** Solar Flare Activity and Satellite Anomaly Causality (ECT-2026-007)
**Date:** 2026-06-14  
**ORCID Identifier:** `0009-0004-9601-5617`

## Charter (one paragraph)

Characterize the causal link between solar weather metrics (solar wind speed, proton flux) and satellite operational anomaly frequencies. This study investigates the causal influence of solar proton flux on telemetry anomaly counts, testing whether space weather indicators causally drive anomalies under propagation lags or if anomalies are driven by internal/spurious cycles, validated by OCCA's causal PC algorithms.

## Primary question (Layer A)

- **Question:** Does solar proton flux (proton_flux) cause satellite telemetry anomalies (anomaly_count) under physical propagation lags?
- **Expected DAG:** `proton_flux -> anomaly_count`
- **Primary metric:** Discovered directed edges and information coefficient.
- **Direction / threshold:** $\alpha = 0.05$ for PC algorithm. The discovered edge must be directed from proton flux to anomaly count, and the absolute correlation must exceed the phase-shuffled Spectral MC null ($p < 0.05$).

## Null / negative controls

- **Null model:** Phase-shuffled Spectral Monte Carlo (FFT surrogate paths).
- **Caps:** Capped at $N = 25$ runs for local smokes (`runs/smoke.yaml`); $N = 1000$ for full remote promotion validation with run ID `charter_space_solar_anomaly_run_01`.

## Truth scope & ethics

- **Scope:** Observational space weather and satellite telemetry data under the **ECT-2026** standard.
- **Data rights:** NOAA space weather logs and satellite telemetry logs.

## Promotion rules

Numbers enter `BEST_ANSWERS_OVERVIEW` (meta) only after `methodology_preamble.assert_run_card` passes in the same environment that produced the artifact. Follow the meta checklist [PROMOTION_CHECKLIST.md](https://github.com/SVG-campus/Research-Apriori/blob/main/docs/PROMOTION_CHECKLIST.md) before editing canonical summaries.
