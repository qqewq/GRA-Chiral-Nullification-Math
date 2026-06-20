"""
Примеры метрик и простых систем.
"""
import numpy as np
from typing import Callable, Tuple

Vector = np.ndarray

def euclidean_metric(a: Vector, b: Vector) -> float:
    return np.linalg.norm(a - b)

def generate_rotations_2d(n: int) -> Tuple[Callable[[Vector], Vector], ...]:
    """Генерирует n поворотов в 2D."""
    rotations = []
    for k in range(n):
        theta = 2 * np.pi * k / n
        cos_t, sin_t = np.cos(theta), np.sin(theta)
        def rot(v, cos_t=cos_t, sin_t=sin_t):
            return np.array([cos_t*v[0] - sin_t*v[1],
                             sin_t*v[0] + cos_t*v[1]])
        rotations.append(rot)
    return tuple(rotations)

# Пример простейшей политики: точка в 3D
sample_policy = np.array([1.0, 2.0, 3.0])
sample_weights = {"a": 0.5, "b": 0.3}
sample_state = {"status": "active"}
