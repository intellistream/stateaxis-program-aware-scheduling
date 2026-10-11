"""Exact activation contract for bounded program-aware scheduling."""

from __future__ import annotations

from dataclasses import dataclass

MOD_ID = "org.vllm-hust.stateaxis-program-aware-scheduling"


@dataclass(frozen=True, slots=True)
class ProgramAwareSchedulingConfig:
    """The only attained-service program authority admitted by StateAxis."""

    enabled: bool = True
    authority: bool = True
    max_programs: int = 64
    max_threads: int = 256
    max_dependencies_per_thread: int = 32
    attained_service_order: bool = True
    ordinary_request_compatibility: bool = True
    generation_bound: bool = True
    request_bound_safe_points: bool = True
    cleanup_on_session_close: bool = True
    selector_budget_us: int = 100
    fail_closed: bool = True

    def __post_init__(self) -> None:
        if self != ProgramAwareSchedulingConfig.__new_default():
            raise ValueError("program-aware scheduling requires the reviewed contract")

    @classmethod
    def __new_default(cls) -> ProgramAwareSchedulingConfig:
        instance = object.__new__(cls)
        for field, value in (
            ("enabled", True),
            ("authority", True),
            ("max_programs", 64),
            ("max_threads", 256),
            ("max_dependencies_per_thread", 32),
            ("attained_service_order", True),
            ("ordinary_request_compatibility", True),
            ("generation_bound", True),
            ("request_bound_safe_points", True),
            ("cleanup_on_session_close", True),
            ("selector_budget_us", 100),
            ("fail_closed", True),
        ):
            object.__setattr__(instance, field, value)
        return instance


def program_aware_scheduling() -> ProgramAwareSchedulingConfig:
    """Return the default-off candidate's admitted ON configuration."""

    return ProgramAwareSchedulingConfig()


__all__ = [
    "MOD_ID",
    "ProgramAwareSchedulingConfig",
    "program_aware_scheduling",
]
