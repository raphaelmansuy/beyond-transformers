# Chapter 10 — World Models & JEPA

## What this chapter teaches

- Prediction ≠ generation: latent predictive objectives vs token sampling.
- JEPA / LeJEPA-style learning in latent space.
- Latent planning for streaming and agent settings.
- Connecting world models to **Dynamic Streamer** planning stubs.

## Example you build

**Latent planning Streamer** — stub that maintains a latent state, predicts the next latent, and chooses a simple action (e.g. skip/process frame) without a full generative decode.

## How to run

```bash
python examples/chapter-10/latent_planning_streamer.py   # stub
```

## Key refs

- I-JEPA — arXiv:2301.08243
