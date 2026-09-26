# Chapter 9 — Energy-Based Models & Dynamic Inference

## What this chapter teaches

- Energy-Based Transformers / EBTs: inference as optimizing an energy.
- The **think loop**: propose → score → revise within a compute budget.
- Self-correction for scalar and agent workloads without claiming free accuracy.
- When dynamic inference is worth the Invoice Impact.

## Example you build

**Self-correcting Scalar** — stub that runs a short energy-descent loop over candidate scalar labels / scores and stops under a budget; log steps vs energy for teaching, not for leaderboard claims.

## How to run

```bash
python examples/chapter-09/self_correcting_scalar.py   # stub
```
