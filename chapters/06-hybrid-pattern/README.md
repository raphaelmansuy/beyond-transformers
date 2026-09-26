# Chapter 6 — The Hybrid Pattern (Attention ⊕ State)

Spine: [`SPINE.md`](SPINE.md) (outline V11 — Packt DOCX not yet available).


## What this chapter teaches

- Why pure Attention or pure state is often insufficient.
- Hybrid patterns in the Samba / Griffin family: local or sparse Attention plus SSM/RNN state.
- How hybrids change the Long-Context Agent design.
- Trade-offs: quality vs memory vs latency (Invoice Impact again).

## Example you build

**Hybrid Long-Context Agent** — stub that interleaves a state update with a small Attention window over recent tokens, compared to Ch4’s pure SSM needle stub.

## How to run

```bash
python examples/chapter-06/hybrid_long_context_agent.py   # stub
```

## Key refs

- Samba — arXiv:2406.07522
- Griffin — arXiv:2402.19427
