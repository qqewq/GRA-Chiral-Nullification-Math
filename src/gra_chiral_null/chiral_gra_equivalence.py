"""
Эквивалентность GRA-обнулёнки и хирального подъёма.
"""
from .chirality_formalism import chiral_pair, Operator
from .gra_null_operator import gra_nullify, GRANullState, Policy, Weights, State
from typing import Tuple

def chiral_reparam(policy: Policy, Z: Operator) -> Policy:
    """Политика становится парой (право, лево)."""
    R, L = chiral_pair(policy, Z)
    return (R, L)

def gra_null_as_chiral(policy: Policy,
                       weights: Weights,
                       state: State,
                       Z: Operator) -> GRANullState:
    """GRA-обнулёнка как хиральный переход: N = (R, L, 0, 0)."""
    return gra_nullify(policy, weights, state,
                       lambda p: chiral_reparam(p, Z))

# Теорема эквивалентности (формально)
theorem_statement = """
Пусть Z - инволютивный оператор зеркального отражения (Z^2 = id).
Тогда для любого объекта X и группы вращений SO такого, что ∀ρ∈SO ρ(X)≠Z(X),
существует изоморфизм между пространством хиральных состояний
и образом оператора GRA-обнулёнки:
    H(X) ≅ N_{Pi}(X, W, S) = (X, Z(X), 0, 0).
"""
