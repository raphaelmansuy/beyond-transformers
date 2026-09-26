# Invoice Impact template

Use this note for **before/after** comparisons against the Chapter 1 Transformer baseline. Fill only measured or clearly labeled placeholder fields — never invent leaderboard numbers.

## Scope

- Workloads: **Efficient Scalar** and **Long-Context Agent** (other examples optional).
- Dimensions: latency, memory / KV footprint, \$/1k tokens (or equivalent), quality on a fixed eval set.

## Template

```markdown
## Invoice Impact — <architecture or chapter>

**Baseline:** Transformer (Ch1) — <model size / context / hardware>

| Metric | Baseline | Candidate | Delta | Notes |
|--------|----------|-----------|-------|-------|
| Latency (p50) | — | — | — | stub |
| Peak memory | — | — | — | stub |
| Cost unit | — | — | — | stub |
| Quality metric | — | — | — | stub; cite eval |

**Scalar:** what changed for Efficient Scalar?
**Agent:** what changed for Long-Context Agent (needle / tools)?

**Caveats:** hardware, batch size, kernel versions, and eval set must match.
```

## Rules

1. Same prompt set and hardware class for before/after.
2. Mark unfinished measurements as `stub`.
3. Link the chapter README and the script path under `examples/chapter-NN/`.
