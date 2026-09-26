# Chapter 3 — Modern Recurrent Neural Networks

## What this chapter teaches

- Why recurrence returned: linear-time decode and constant-size state.
- **xLSTM** and **RWKV-7** ideas at a high level (gates, channel/time mixing).
- The **WKV** kernel intuition (what makes RWKV fast in practice).
- Fitting modern RNNs to the **Efficient Scalar** workload.

## Example you build

**Efficient Scalar with RWKV** — a stub that swaps the Ch1 Attention baseline for an RWKV-style recurrent step on a tiny scalar/classification stream, with an Invoice Impact skeleton.

## How to run

```bash
python examples/chapter-03/efficient_scalar_rwkv.py   # stub
```

## Key refs

- RWKV — arXiv:2305.13048
- xLSTM — arXiv:2405.04517
