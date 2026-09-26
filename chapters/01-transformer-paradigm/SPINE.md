# Spine — Chapter 1: The Transformer Paradigm (2017–2024)

**Source:** Packt-style manuscript (Notion: Chapter 1 — Revised / B38257_01_*.docx). Headings only — not the manuscript.

**Source class:** Packt DOCX (Ch1–3)

## Headings

1. Technical requirements
2. Tracing How Transformers Won Training
   - Identifying the Three Properties Behind Transformer Dominance
   - Introducing the Reference Production Stack
   - Comparing the Inductive Biases of CNNs, RNNs, and Transformers
   - Deriving Scaled Dot-Product Attention
   - Mapping the Forward Pass Costs Stage by Stage
   - Framing the Transformer as the Measurement Baseline
   - Setting Up the Keep-Versus-Confront Framework
3. Generating Your First Inference Scorecard
   - Defining the Vocabulary We Measure In
   - Working with Two Speed Limits on One Chip
   - Pinning Down the Worst Case
   - Running the Scorecard
   - Running the Same Card on a Small, Fast Model
   - Reading the Card: Ceiling Versus Reality
   - Indexing the Four Walls at a Glance
4. Deriving the Physics of Inference Costs
   - Prefill / Memory / Bandwidth walls + Recall check
5. Stress-Testing the Four Workloads
   - Efficient Scalar · Long-Context Agent · Structural Reasoner · Dynamic Streamer
   - Assembling the Master Matrix
6. Making the Scorecard Yours
7. Summary

## Named examples / scripts (from manuscript + outline)

- `examples/chapter-01/nano_transformer.py` — tiny Attention baseline
- `examples/chapter-01/invoice_summary.py` — Invoice Impact baseline rows
- `examples/chapter-01/limit4_recall_demo.py` — Wall 4 recall demo
