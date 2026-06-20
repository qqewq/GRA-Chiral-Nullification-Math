"""
Численная проверка эквивалентности GRA-обнулёнки и хиральности.
"""
import numpy as np
from ..chirality_formalism import chiral_pair, mirror_operator_nd
from ..gra_null_operator import gra_null_as_chiral

def verify_equivalence_on_random_points(dim=3, n_trials=1000):
    """Для случайных точек в R^dim проверяем, что обнулёнка всегда даёт хиральную пару."""
    Z = mirror_operator_nd(-1)
    for _ in range(n_trials):
        x = np.random.randn(dim)
        weights = {"mass": 1.0}
        state = {"id": 0}
        result = gra_null_as_chiral(x, weights, state, Z)
        R, L = result.policy
        # Проверка: L == Z(R) и R == x
        assert np.allclose(L, Z(R)), f"Нарушено: L={L}, Z(R)={Z(R)}"
        assert np.allclose(R, x)
    print(f"Пройдено {n_trials} проверок: GRA-обнулёнка = хиральный подъём.")

if __name__ == "__main__":
    verify_equivalence_on_random_points()
