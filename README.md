# stateaxis-program-aware-scheduling

Extension ID: `org.vllm-hust.stateaxis-program-aware-scheduling`

This repository owns the independent MOD boundary for StateAxis issue
[#12](https://github.com/Qixin-Gaoke/stateaxis/issues/12): bounded,
generation-aware attained-service scheduling across agent program threads.
Version `0.2.0` is an active Manifest 0.3 contract for the existing StateAxis
host mechanism. It remains default-off and is activated only through Extension
Manager/ECPA with the exact research-manifest digest.

## Evidence boundary

Status: **historical matched negative, active experimental, not
performance-qualified**.

In the frozen Qwen2.5-14B BF16 high-fan-out cell, program throughput improved
`0.355%`, program-completion P50 improved `11.973%`, and attained-service
fairness improved `12.0%`. Those component changes did not pass the registered
gate: program-tail gains were below `15%`, and ordinary-request TPOT P99
regressed `8.082%` against a `5%` guard. This result applies only to that cell;
it is neither a general speedup nor evidence that other program shapes cannot
benefit.

Negative, failed, and inconclusive attempts are retained. The copied evidence
and SHA-256 are recorded in `PROVENANCE.json`. A compact machine-readable R7/R9
bundle, including all six run identities, is under
`evidence/issue12-program-performance-20260815-r7/`; see `EVIDENCE.md` for the
index.

## Activation contract

The admitted ON contract fixes the program/thread/dependency bounds,
attained-service order, ordinary-request compatibility, generation binding,
request-bound safe points, selector budget, close-time cleanup, and fail-closed
behavior. It requires
`org.vllm-hust.stateaxis-session-lifecycle >=0.2,<0.3`; both MODs must be enabled
in the same Manager plan. Direct `STATE_ENGINE_ISSUE12_*` activation is rejected
by the StateAxis host.

```bash
python -m pip install .
vllm-hust-ext extension inspect org.vllm-hust.stateaxis-program-aware-scheduling
vllm-hust-ext extension check org.vllm-hust.stateaxis-program-aware-scheduling
vllm-hust-ext extension plan org.vllm-hust.stateaxis-program-aware-scheduling
vllm-hust-ext run --dry-run -- /path/to/native_state_engine ...
```

Rollback is omission: remove this MOD from the Manager plan. StateAxis then uses
ordinary scheduling; the session-lifecycle dependency can be independently kept
or removed subject to other dependents.

## Validate

```bash
python -m pip install -e '.[test]'
pytest -q
```

Maintainer: Shuhao Zhang (Tony), directly responsible; no advisor is declared.
