# Issue #12 R9 immutable-raw analysis

- Source: R7 real-NPU 1+1 gate plus fresh-process 3+3 on NPU5.
- Correctness: 234/234 formal requests exact; lifecycle exact; fallback zero.
- Program completion P50/P95/P99 delta: -11.973% / -0.378% / -0.378%.
- Program throughput delta: +0.355%.
- Ordinary TPOT P99 delta: +8.082%, failing the frozen 5% guard.
- Selector P99: 43.631 us, passing the 100 us budget.
- Peak HBM: 53,534 MiB in both arms.
- Frozen 650 ms SLO: zero completions in both arms; denominator rejected.
- Decision: `matched_negative`; default-off; no statistical, general speedup, or vLLM comparison claim.
