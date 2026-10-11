# Examples — Chapter 13

CPU-smoke for the **Invoice Impact leaderboard** schema. The runner
conceptually aggregates Chapters 3–12 Invoice rows versus the Chapter 1
**8B GQA-8** scorecard. Companion memory units are **GiB** (2³⁰).

This smoke prints the labelled table / schema only. **Fills stay empty.**
Do not invent numbers, SOTA tables, or timings.

## Label set

Every cell label must be one of:

- `modelled`
- `measured`
- `reproduced-from-source`
- `stub`

Filled-cell format (when a value exists): `<value> · <label>`. Empty fills
print as `stub`.

## Locks

- Baseline preset: **8B GQA-8**
- Memory: **GiB** (2³⁰). Paper “GB” only in `reproduced-from-source` cells.
- Required workloads: Efficient Scalar, Long-Context Agent
- Optional workloads (columns kept): Structural Reasoner, Dynamic Streamer
- MQAR and RULER columns on state / hybrid rows (empty or pass/fail placeholder)
- Needle **5,401** is illustrative · `modelled` only — not a measured accuracy
- Bi-Mamba **50.6%**, if cited, is `reproduced-from-source` (arXiv:2411.11843) — never a measured companion result
- Packt-safe: no customer or company names

Template: [`../templates/invoice-impact.md`](../templates/invoice-impact.md).

```bash
python3 examples/chapter-13/invoice_leaderboard.py
```

Chapter guide: [`chapters/13-evaluation-benchmarks/`](../../chapters/13-evaluation-benchmarks/).
