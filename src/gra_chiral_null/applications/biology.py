"""
Биологическая гомохиральность: GRA-обнулёнка объясняет выбор L-аминокислот.
Расчёт: хиральный потенциал как функция эволюционной приспособленности.
"""
import numpy as np
from ..chirality_formalism import chiral_pair, mirror_operator_nd
from ..gra_null_operator import gra_null_as_chiral

def homochirality_emergence(fitness_landscape: callable, Z):
    """
    Эволюция политики (генетический код) под действием обнулёнки:
    все симметричные стратегии подавляются, остаётся чистая хиральность.
    """
    # начальная политика - рацемическая смесь (симметричная)
    policy_racemic = np.array([0.5, 0.5])  # доли L и D
    weights = {"L": 0.5, "D": 0.5}
    state = "prebiotic"
    result = gra_null_as_chiral(policy_racemic, weights, state, Z)
    # result.policy = (R, L) -> теперь чистая пара
    print("После GRA-обнулёнки:", result.policy)
    # Предсказание: одна энантиомерная форма полностью исчезает
    return result.policy

# Зеркало: отражение L <-> D
Z_bio = mirror_operator_nd(0)  # первая координата - L/D
homochirality_emergence(None, Z_bio)
