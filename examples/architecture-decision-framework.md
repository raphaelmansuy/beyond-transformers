# Architecture decision framework (Chapter 2)

Short triage matching the 2026 taxonomy: **Generative**, **Predictive**, and **Energy-Based** families. Use with the stub `examples/chapter-02/triage.py`.

## Questions (in order)

1. **Output type** — tokens / continuous latents / energy landscape over candidates?
2. **Context shape** — short & dense, long & sparse, or streaming?
3. **State need** — pure attention, recurrent / SSM state, or hybrid Attention ⊕ State?
4. **Structure** — flat sequence vs graph / KG constraints?
5. **Inference budget** — single forward, or a think / verify loop (EBM)?
6. **Deploy target** — datacenter, edge, or mobile (see Ch12 compression)?

## Rough map

| Need | First candidates |
|------|------------------|
| Generative next-token, short–mid context | Transformer baseline; RetNet / hybrid later |
| Long context, linear-ish memory | Mamba / SSM; Samba–Griffin hybrids |
| Streaming scalar / cheap decode | RWKV / xLSTM (Efficient Scalar) |
| Multimodal real-time | MambaVision / VAMBA-style (Dynamic Streamer) |
| Structured constraints | GNN + ConstraintLLM (Structural Reasoner) |
| Self-correcting / search at decode | EBM think loop (Ch9) |
| Latent planning | JEPA-style world model (Ch10–11) |

## Output of triage

Record: chosen family, running example(s) touched, and a scorecard / Invoice Impact stub (Ch3+) if replacing the Ch1 baseline rows.
