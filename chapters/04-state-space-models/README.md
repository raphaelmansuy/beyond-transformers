# Chapter 4 — State Space Models (SSMs)

## What this chapter teaches

- From S4-style continuous SSMs to **selective** discrete models (Mamba).
- Selectivity: why content-dependent state updates matter for language and agents.
- Long-context behavior: needle-in-haystack intuition without fake scores.
- MoE-Mamba as a capacity × efficiency sketch.

## Example you build

**Long-Context Agent — needle stub** — a placeholder pipeline that feeds a long synthetic context to an SSM-style state update and reports whether a planted needle token is recoverable (toy accuracy only). Optional MoE-Mamba routing stub.

## How to run

```bash
python examples/chapter-04/long_context_agent_needle.py   # stub
python examples/chapter-04/moe_mamba_sketch.py            # stub
```

## Key refs

- S4 — arXiv:2111.00396
- Mamba — arXiv:2312.00752
