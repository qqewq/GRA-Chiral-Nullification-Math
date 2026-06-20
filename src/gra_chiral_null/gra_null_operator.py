"""
GRA-обнулёнка: оператор N(Pi, W, S) -> (Pi', 0, 0).
"""
from dataclasses import dataclass
from typing import Dict, Any, Callable

Policy = Any
Weights = Dict[str, float]
State = Any

@dataclass
class GRANullState:
    policy: Policy
    weights: Weights
    state: State

def gra_nullify(policy: Policy,
                weights: Weights,
                state: State,
                reparam: Callable[[Policy], Policy]) -> GRANullState:
    """
    Обнуление: переопределяем политику, зануляем веса и состояние.
    """
    new_policy = reparam(policy)
    zero_weights = {k: 0.0 for k in weights}
    zero_state = None
    return GRANullState(policy=new_policy,
                        weights=zero_weights,
                        state=zero_state)
