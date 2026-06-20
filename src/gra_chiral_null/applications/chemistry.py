"""
Химическая хиральность: катализ и селективность.
Расчёт: энантиомерный избыток как функция оператора обнулёнки.
"""
import numpy as np
from ..chirality_formalism import chiral_measure
from ..metrics_and_examples import euclidean_metric

def enantiomeric_excess(catalyst_profile: np.ndarray) -> float:
    """
    Профиль катализатора как вектор в пространстве свойств,
    зеркало меняет знак асимметричного параметра.
    """
    Z = lambda x: x * np.array([1, -1])  # отражение по второму свойству
    chi = chiral_measure(catalyst_profile, Z, euclidean_metric)
    ee = 1 - np.exp(-chi)  # ee растёт с хиральностью
    return ee

cat = np.array([0.8, 0.2])
print(f"Энантиомерный избыток: {enantiomeric_excess(cat):.2%}")
