# Issue #12 high-fan-out program scheduling closure — 2026-08-15

> **Point-in-time report — not current repository status.** Current
> classification lives in [`NATIVE_ENGINE_STATUS.md`](../../NATIVE_ENGINE_STATUS.md).

## Decision

Issue #12's original high-fan-out performance acceptance is complete with a
matched negative result. The default-off attained-service authority is exact,
bounded, lifecycle-clean and selector-budget compliant, but it misses the 15%
program-tail/throughput target and regresses the frozen ordinary-request TPOT
P99 guard. It remains an experimental opt-in hook and is not a speedup or vLLM
comparison claim.

## Frozen scope and identity

The real-NPU campaign used the local official
`quay.io/ascend/vllm-ascend:v0.23.0rc1-openeuler` image at
`sha256:f4c89c293e076453e9eef9edb5fb9669740dccbd3c48619a9f976d775fc29b81`,
Qwen2.5-14B BF16, state capacity 68, 256 physical blocks, max batch one and one
fresh server/worker process per run. R7 aggregate identity is
`6e7a87409308aaa9715d7513ffd706e75189b4a027fbc74f4fb700eb3dd0c1a2`;
the frozen workload is
`f4758faf4061e63767ae8421fe24f5dd86a0bc920bf0c71d1606f06100bb675f`.

Each run contains four already-attained programs with four-way fan-out, twelve
new programs, four ordinary compatibility requests, and a sequential
three-step topology replay from OpenBMB ToolBench. The public source is fixed
at commit `d56fdd89faf8c91fa135090b212bb9057ee5cfc2`, Git blob
`79d39226f85e96d937ba8ea8e693862793c36e42`, source SHA-256
`76a77721640045e07142c669008611e6b82b25007c73427aec771adbf9dd9841`.
Only topology and tool-wait timing are copied; source observations and contact
data are not included.

The R9 analysis is bound to every formal result and raw request file by
identity `f47f5ff6dcb390b645bf6be70f80dca1576d9d282d0aa36ac406959015b3ef1a`.
It changes no NPU input or decision predicate.

## Correctness and lifecycle

The 1+1 gate and all six formal runs completed exact outputs and lifecycle
checks. The formal matrix contains 234/234 exact requests; all 16 measured
programs and all 12 ordinary requests per arm completed, the public trace was
exact, and close left zero active programs or threads. Candidate authority
applied 129 times per run, with 29 selection changes across the three runs and
zero fallback. Control applied no authority. Offline validation passed all 238
Rust library tests, every binary test, all-target check, and the FIFO
compatibility regression. There was no mid-request preemption or recomputation;
state hits were zero in both arms.

## Matched 3+3 result

Values below are the median across three fresh-process per-run summaries.

| Metric | Control | Candidate | Delta / decision |
|---|---:|---:|---:|
| program completion P50 | 2,467.839 ms | 2,172.363 ms | -11.973%; below 15% gate |
| program completion P95 | 2,652.371 ms | 2,642.347 ms | -0.378%; below 15% gate |
| program completion P99 | 2,668.741 ms | 2,658.649 ms | -0.378% |
| program throughput | 5.7477/s | 5.7680/s | +0.355%; below 15% gate |
| request throughput | 11.4953/s | 11.5361/s | +0.355% |
| all-request TTFT P50 / P95 / P99 | 564.865 / 1,087.616 / 1,134.134 ms | 428.208 / 945.441 / 992.299 ms | lower |
| all-request TPOT P50 / P95 / P99 | 822.727 / 855.798 / 858.473 ms | 893.880 / 926.022 / 932.206 ms | P99 +8.589% |
| ordinary TTFT P99 | 1,144.856 ms | 1,003.151 ms | -12.378% |
| ordinary TPOT P99 | 812.371 ms | 878.030 ms | +8.082%; fails 5% guard |
| ordinary scheduler wait P99 | 1,114.379 ms | 972.346 ms | -12.745% |
| Jain attained-service fairness at 650 ms | 0.2232 | 0.2500 | +12.0% |
| actual selector P99 | 24.585 us | 43.631 us | candidate below 100 us budget |
| AICore utilization P95 | 83.4% | 84.7% | sampled |
| NPU utilization P95 | 95.1% | 100.0% | sampled |
| peak HBM | 53,534 MiB | 53,534 MiB | unchanged |
| request-throughput CV | 0.046% | 0.342% | low dispersion |

The frozen 650 ms SLO goodput is zero in every run of both arms. R8 therefore
marks that branch `rejected_zero_control_denominator`; it cannot become positive
evidence through division by zero. R9 adds the omitted complete metric set from
the same immutable raw files without changing this decision. The remaining
preregistered P95 branch misses its threshold, and ordinary TPOT P99 fails its
guard, so the final classification is `matched_negative`.

## Evidence custody and rejected attempts

Accepted requests, metrics, NPU/HBM samples, logs, cleanup, R9 result and
analysis identity are under
`results/issue12-program-performance-20260815-r7/`. R5 is preserved as a
pre-freeze resident-plan rejection caused by an over-conservative 40×16 block
projection. R6 is preserved as a launcher-enum failure before server/NPU
execution. R7 completed all NPU runs but its first analyzer exited because SLO
goodput was unmeasurable; R8 fixed that fail-closed decision, and R9 only
completed the required aggregate metric inventory. No run was deleted, no SLO
was retuned, and no NPU run was repeated for analysis.
