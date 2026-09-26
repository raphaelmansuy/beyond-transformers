"""Chapter 1 — inference scorecard / four-walls accounting stub.

Walls: Prefill/Time, Memory, Bandwidth, Recall.
Apply the same card across Efficient Scalar, Long-Context Agent,
Structural Reasoner, and Dynamic Streamer.

Invoice Impact before/after protocol starts in Chapter 3+.
"""

WALLS = ("prefill_time", "memory", "bandwidth", "recall")
WORKLOADS = (
    "efficient_scalar",
    "long_context_agent",
    "structural_reasoner",
    "dynamic_streamer",
)


def main() -> None:
    print("inference_accounting stub")
    print("walls:", ", ".join(WALLS))
    print("workloads:", ", ".join(WORKLOADS))
    print("status: stub — fill with measured or clearly labeled placeholder fields")


if __name__ == "__main__":
    main()
