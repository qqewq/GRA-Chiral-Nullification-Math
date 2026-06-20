"""
Чистая математика хиральности.
Объекты, оператор зеркала, группа вращений, проверка хиральности.
"""
from typing import Callable, Tuple, Any, List
import numpy as np

X = Any
Operator = Callable[[X], X]

def mirror_operator_nd(axis: int = -1):
    """Оператор отражения по заданной оси в R^n."""
    def Z(x: np.ndarray) -> np.ndarray:
        y = x.copy()
        y[axis] = -y[axis]
        return y
    return Z

def is_chiral(x: X, Z: Operator, rotations: Tuple[Operator, ...]) -> bool:
    """
    Объект хирален, если ни одно вращение не переводит его в зеркальный образ.
    """
    zx = Z(x)
    for rho in rotations:
        if np.allclose(rho(x), zx):
            return False
    return True

def chiral_pair(x: X, Z: Operator) -> Tuple[X, X]:
    """Правая и левая хиральности."""
    return x, Z(x)

def chiral_measure(x: X, Z: Operator, metric: Callable[[X, X], float]) -> float:
    """Количественная мера хиральности: расстояние между x и Z(x)."""
    return metric(x, Z(x))
