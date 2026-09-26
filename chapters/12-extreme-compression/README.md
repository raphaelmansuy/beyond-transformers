# Chapter 12 — Extreme Compression & Quantization

Spine: [`SPINE.md`](SPINE.md) (outline V11 — Packt DOCX not yet available).


## What this chapter teaches

- Why linear-time / stateful models compress differently than Transformer KV caches.
- Bi-Mamba and binary / low-bit sketches for SSMs.
- RWKV-oriented **mobile quantization** for Efficient Scalar.
- Measuring size and latency on-device vs Ch1 baseline (Invoice Impact).

## Example you build

**RWKV mobile quant stub** — fake weights → int8 (or binary sketch) pack/unpack, report bytes and a toy decode latency proxy for Efficient Scalar. Optional Bi-Mamba sketch.

## How to run

```bash
python examples/chapter-12/rwkv_mobile_quant.py   # stub
python examples/chapter-12/bi_mamba_sketch.py     # stub
```
