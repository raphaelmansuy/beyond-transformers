"""Chapter 1 — inference scorecard / four-walls accounting stub.

Walls: Prefill/Time, Memory, Bandwidth, Recall.
Apply the same card across Efficient Scalar, Long-Context Agent,
Structural Reasoner, and Dynamic Streamer.

Companion locks: Transformer preset is 8B GQA-8; memory units are GiB
(2**30). Do not invent timings. Invoice Impact starts in Chapter 3+.
"""

PRESET = "8B GQA-8"
MEMORY_UNIT = "GiB"  # 2**30 bytes; paper "GB" only in reproduced-from-source cells
WALLS = ("prefill_time", "memory", "bandwidth", "recall")
WORKLOADS = (
    "efficient_scalar",
    "long_context_agent",
    "structural_reasoner",
    "dynamic_streamer",
)


def main() -> None:
    print("inference_accounting stub")
    print("preset:", PRESET)
    print("memory_unit:", MEMORY_UNIT)
    print("walls:", ", ".join(WALLS))
    print("workloads:", ", ".join(WORKLOADS))
    print("status: stub — fill with measured or clearly labeled placeholder fields")


if __name__ == "__main__":
    main()
