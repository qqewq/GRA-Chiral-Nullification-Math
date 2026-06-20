"""
Межполушарная асимметрия: GRA-обнулёнка формирует латерализацию.
"""
import numpy as np
from ..chirality_formalism import chiral_pair

def brain_lateralization(neural_state: np.ndarray, Z: callable):
    """Модель активации левого/правого полушария как хиральная пара."""
    R, L = chiral_pair(neural_state, Z)
    return R, L

# Зеркало: переворот по сагиттальной оси
Z_brain = lambda x: np.flip(x)  # для 1D массива активации
state = np.array([0.9, 0.2])  # левое активнее
left, right = brain_lateralization(state, Z_brain)
print("Левое полушарие:", left, "Правое:", right)
