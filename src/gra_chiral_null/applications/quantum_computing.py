"""
Квантовые вычисления: кубит как хиральный объект, гейты как вращения.
Обнулёнка = проекция на хиральное подпространство.
"""
import numpy as np
from ..chirality_formalism import is_chiral, chiral_measure

def chiral_qubit_state(state: np.ndarray) -> bool:
    """Проверка, является ли состояние кубита хиральным (не самосопряжённым)."""
    Z = lambda x: np.conj(x)
    # Группа SU(2) вращений аппроксимируется конечным набором
    rotations = (
        lambda x: x,
        lambda x: np.array([x[1], -x[0]]),
        lambda x: np.array([-x[0], -x[1]]),
        lambda x: np.array([-x[1], x[0]]),
    )
    return is_chiral(state, Z, rotations)

psi = np.array([1/np.sqrt(2), 1j/np.sqrt(2)])
print("Кубит хирален:", chiral_qubit_state(psi))
