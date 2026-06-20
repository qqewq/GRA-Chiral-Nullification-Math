"""
Эстетическая хиральность: золотое сечение и зеркальная гармония.
"""
import numpy as np
from ..chirality_formalism import chiral_measure

def beauty_measure(composition_vector: np.ndarray) -> float:
    """
    Эстетическая привлекательность коррелирует с хиральной асимметрией.
    """
    Z = lambda v: np.array([1/v[0], v[1]]) if v[0]!=0 else v  # инверсия пропорции
    chi = chiral_measure(composition_vector, Z, lambda a,b: np.linalg.norm(a-b))
    return 1 - np.exp(-chi)  # 0..1

# Пример: пропорции лица
face_proportions = np.array([1.618, 1.0])  # золотое сечение
print("Индекс красоты:", beauty_measure(face_proportions))
