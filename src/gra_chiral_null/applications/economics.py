"""
Экономическая асимметрия: хиральность рынка.
Обнулёнка предсказывает кризисы как переход через хиральный порог.
"""
import numpy as np
from ..chirality_formalism import chiral_measure

def market_crisis_probability(supply_demand_vector: np.ndarray) -> float:
    """
    Вектор (спрос, предложение), зеркало = обмен местами с инверсией тренда.
    Мера хиральности → вероятность обвала.
    """
    Z = lambda v: np.array([v[1], v[0]])  # спрос-предложение
    chi = chiral_measure(supply_demand_vector, Z, lambda a,b: np.abs(a[0]-b[0]) + np.abs(a[1]-b[1]))
    return 1 / (1 + np.exp(-5*(chi - 1.0)))  # сигмоида

sd = np.array([1.2, 0.8])  # небольшой дисбаланс
print(f"Вероятность кризиса: {market_crisis_probability(sd):.2%}")
