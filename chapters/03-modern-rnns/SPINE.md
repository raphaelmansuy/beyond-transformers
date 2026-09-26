# Spine — Chapter 3: Modern Recurrent Neural Networks (The Gated Linear Pattern)

**Source:** Packt Style DOCX (`B38257_03_Packt`). Headings only — not the manuscript.

**Source class:** Packt DOCX (Ch1–3)

## Headings

1. Technical requirements
2. Understanding why recurrence is returning
   - Comparing attention memory with recurrent state
   - Identifying the serving pressure behind the return
   - Comparing recurrence with bounded attention windows
   - Revisiting the weaknesses of classical RNNs
   - Defining the narrower production thesis
3. Building gated linear recurrence from first principles
   - Starting with a linear state update
   - Adding gates for selective memory
   - Tracing one update by hand
   - Understanding matrix-valued memory
   - Recognizing the remaining recall limit
4. Extending memory with xLSTM
   - Revisiting LSTM memory
   - Using exponential gates safely
   - Distinguishing sLSTM from mLSTM
   - Reading the scaling evidence carefully
   - Mapping xLSTM to production workloads
5. Evolving state dynamically with RWKV-7 Goose
   - Combining recurrence with Transformer-style blocks
   - Understanding diagonal-plus-rank-one updates
   - Applying the generalized delta rule
   - Interpreting formal expressivity claims
   - Separating paper claims from local measurements
6. Engineering parallel training and efficient inference
   - Separating training from inference execution
   - Processing sequences in chunks
   - Understanding kernels and memory bandwidth
   - Recognizing that nonlinear recurrence is also changing
   - Capturing the decode path with CUDA Graphs
   - Choosing precision for a long-lived recurrent state
   - Persisting recurrent state across restarts and redeployments
   - Resetting state at stream discontinuities
   - Serving many streams at once
   - Designing a reproducible benchmark harness
7. Designing The Efficient Scalar rebuild
   - Defining the workload and service level objective
   - Establishing an architecture-derived memory model
   - Costing the rebuild and the training-to-serving gap
   - Implementing the recurrent scalar model
   - Testing correctness before speed
8. Defining the invoice protocol and routing future workloads
   - Ordering the measurement runs
   - Naming the remaining weakness
   - Carrying the lesson to other running examples
9. Summary
10. Further reading

## Technical requirements (distilled)

- Python 3.11+; PyTorch 2.5+ (GPU benchmarks need CUDA-capable hardware)
- Examples under `examples/chapter-03/`
- Named files: `kv_cache_estimate.py`, `gated_recurrence.py`, `test_gated_recurrence.py`, `invoice_benchmark.py`

## Named examples / scripts

- `examples/chapter-03/kv_cache_estimate.py`
- `examples/chapter-03/gated_recurrence.py`
- `examples/chapter-03/test_gated_recurrence.py`
- `examples/chapter-03/invoice_benchmark.py`

## Invoice Impact (starts here)

Rebuild **Efficient Scalar** with gated recurrence / RWKV; record before/after vs the Chapter 1 Transformer scorecard baseline. Template: [`examples/templates/invoice-impact.md`](../../examples/templates/invoice-impact.md).
