# Chapter 5 — Comparative Dynamics

Spine: [`SPINE.md`](SPINE.md) (outline V11 — Packt DOCX not yet available).


## What this chapter teaches

- How Linear Attention, SSMs, and modern RNNs relate as dynamical systems.
- Honest evaluation: **MQAR** and copying tasks (what each family can and cannot do).
- RetNet as a bridge between attention-like and recurrent views.
- Why comparative dynamics beat single-number marketing curves.

## Example you build

A **toy MQAR / copying harness** that runs the same synthetic sequences through placeholder Linear-Attention, SSM, and RNN step functions and prints qualitative pass/fail — no invented SOTA tables.

## How to run

```bash
python examples/chapter-05/mqar_copying_harness.py   # stub
```

## Key refs

- RetNet — arXiv:2307.08691
