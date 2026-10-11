# Chapter 13 — Evaluation & Benchmarks (2025–2026)

Spine: [`SPINE.md`](SPINE.md) (outline V11 — Packt DOCX not yet available).


## What this chapter teaches

- Why perplexity alone is not enough for agents, long context, and structure.
- Task suites: needle / MQAR / copying, tool use, constraint satisfaction, streaming lag.
- Building an **invoice leaderboard** layout (columns only — fill with your measurements).
- Honesty rules: hardware, seeds, and stub vs real weights.

## Example you build

**Invoice leaderboard scaffold** — a labelled schema runner that conceptually aggregates Invoice Impact rows for Scalar and Agent (Reasoner / Streamer columns kept, optional) across Chapters 3–12. Empty cells until you measure; do not invent fills.

## How to run

```bash
python3 examples/chapter-13/invoice_leaderboard.py   # schema + labels; fills empty
```
