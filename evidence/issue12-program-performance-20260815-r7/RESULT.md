# Historical R7/R9 matched real-NPU result

This is the accepted issue #12 high-fan-out campaign: Qwen2.5-14B BF16,
Ascend 910B2, max batch one, and three fresh processes per arm. R9 completed the
metric inventory from the immutable R7 raw runs; it did not rerun or retune them.

| Metric | Control median | Candidate median | Delta / gate |
|---|---:|---:|---:|
| Program completion P50 | 2,467.839 ms | 2,172.363 ms | -11.973%; below 15% target |
| Program completion P95 | 2,652.371 ms | 2,642.347 ms | -0.378%; below 15% target |
| Program throughput | 5.7477/s | 5.7680/s | +0.355%; below 15% target |
| Ordinary-request TPOT P99 | 812.371 ms | 878.030 ms | +8.082%; fails 5% guard |
| Ordinary-request TTFT P99 | 1,144.856 ms | 1,003.151 ms | -12.378% |
| Jain fairness at 650 ms | 0.2232 | 0.2500 | +12.0% |
| Peak HBM | 53,534 MiB | 53,534 MiB | unchanged |

All six formal runs were exact and lifecycle-clean: 234/234 requests completed,
all measured programs and ordinary compatibility requests completed, and close left
zero active programs or threads. Candidate authority applied 129 times per run,
changed selection 29 times across the campaign and recorded zero fallback.

The classification is nevertheless `matched_negative`: the registered benefit
threshold was missed and ordinary-request TPOT P99 breached its guard. Both arms had
zero goodput at the frozen 650 ms SLO, so the goodput ratio was correctly rejected
for a zero control denominator. This result applies only to the frozen high-fan-out
workload and does not prove other program shapes cannot benefit. It also does not
qualify the later v0.2.0 ECPA contract.
