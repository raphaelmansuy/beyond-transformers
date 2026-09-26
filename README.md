# Beyond Transformers

Companion code and scaffolds for **Beyond Transformers: Architectures for the Next Generation of Generative AI** (Packt).

**Authors:** Raphaël Mansuy & Annaëlle Mansuy

## Mission

This is an **open companion** — not the full manuscript. Each chapter folder holds a short README (what you learn + the example you build) and placeholder example paths. Content follows the book outline (V11) and reflects **September 2026** ML engineering practice: post-Transformer stacks (SSMs, hybrids, JEPA-style world models, agentic loops, and evaluation beyond perplexity).

## Why “beyond” Transformers?

Transformers remain the baseline (Part I). The rest of the book maps the 2026 architectural taxonomy — modern RNNs, state-space models, hybrids, multimodal variants, GNNs, energy-based inference, world models, agents, compression, and evals — so you can choose the right inductive bias for the job.

## Running examples

Four examples thread through the book. Reuse them; do not invent parallel demos.

| Example | Role |
|--------|------|
| **Efficient Scalar** | Cheap, streaming scalar / classification workloads (RWKV, quantized mobile paths) |
| **Long-Context Agent** | Needle-in-haystack and long-horizon tool use (SSM / hybrid attention⊕state) |
| **Structural Reasoner** | Graph / KG constraints and structured outputs (GNN + ConstraintLLM) |
| **Dynamic Streamer** | Real-time multimodal streams (e.g. 60 fps vision–language pipelines) |

## Invoice Impact

Chapter 1 introduces an **Invoice Impact** mechanism: a before/after cost–latency–quality note versus the Transformer baseline for Scalar and Agent. Use the template in [`examples/templates/invoice-impact.md`](examples/templates/invoice-impact.md). Do not invent fake leaderboard numbers.

## Architecture triage

Chapter 2’s decision framework lives at [`examples/architecture-decision-framework.md`](examples/architecture-decision-framework.md) (and the stub `triage.py` under that chapter’s examples).

## Chapters

| # | Folder | Title |
|---|--------|-------|
| 1 | [chapters/01-transformer-paradigm](chapters/01-transformer-paradigm) | The Transformer Paradigm (2017–2023) |
| 2 | [chapters/02-architectural-taxonomy-2026](chapters/02-architectural-taxonomy-2026) | The Architectural Taxonomy of 2026 |
| 3 | [chapters/03-modern-rnns](chapters/03-modern-rnns) | Modern Recurrent Neural Networks |
| 4 | [chapters/04-state-space-models](chapters/04-state-space-models) | State Space Models (SSMs) |
| 5 | [chapters/05-comparative-dynamics](chapters/05-comparative-dynamics) | Comparative Dynamics |
| 6 | [chapters/06-hybrid-pattern](chapters/06-hybrid-pattern) | The Hybrid Pattern (Attention ⊕ State) |
| 7 | [chapters/07-multimodal-hybrids](chapters/07-multimodal-hybrids) | Multimodal Hybrids |
| 8 | [chapters/08-gnns-structured-reasoning](chapters/08-gnns-structured-reasoning) | GNNs & Structured Reasoning |
| 9 | [chapters/09-energy-based-models](chapters/09-energy-based-models) | Energy-Based Models & Dynamic Inference |
| 10 | [chapters/10-world-models-jepa](chapters/10-world-models-jepa) | World Models & JEPA |
| 11 | [chapters/11-agentic-loops](chapters/11-agentic-loops) | Agentic Loops & Hierarchical Planning |
| 12 | [chapters/12-extreme-compression](chapters/12-extreme-compression) | Extreme Compression & Quantization |
| 13 | [chapters/13-evaluation-benchmarks](chapters/13-evaluation-benchmarks) | Evaluation & Benchmarks (2025–2026) |
| 14 | [chapters/14-unified-architectures](chapters/14-unified-architectures) | Toward Unified Architectures (2026–2030) |
| 15 | [chapters/15-societal-ethical](chapters/15-societal-ethical) | Societal & Ethical Implications |

Example stubs live under `examples/chapter-NN/` and point back to the matching chapter README.

## Stance (Sept 2026)

Treat the Transformer as the **measured baseline**, then pick SSM / hybrid / JEPA / agent / eval tooling for the workload. Prefer honest comparative dynamics (MQAR, copying) over marketing curves.

## License

MIT — see [`LICENSE`](LICENSE). Contributions welcome via [`CONTRIBUTING.md`](CONTRIBUTING.md).

Publisher: Packt. This repo does not redistribute the book manuscript.
