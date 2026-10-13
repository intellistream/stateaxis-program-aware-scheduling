# Evidence index

The current MOD is active experimental and not performance-qualified.

- `evidence/ISSUE12_PROGRAM_PERFORMANCE_CLOSURE_20260815.md` preserves the
  historical matched 3+3 real-NPU result. It is exactness- and
  lifecycle-positive but performance-negative in its frozen cell.
- `evidence/issue12-program-performance-20260815-r7/` preserves the
  machine-readable R9 aggregate, frozen identity, six run identities, hardware
  selection and closure audits. `RESULT.md` states the gate decision and limits.
- `evidence/on-off-preflight-20261010/RESULT.json` preserves the earlier inert
  admission rejection and is not an ON/OFF result.

The historical candidate changed the schedule 29 times and applied authority
129 times per run with zero fallback. Program throughput improved only 0.355%
and ordinary-request TPOT P99 regressed 8.082%, so it failed the registered
performance gate. No result in this repository establishes a general gain.
