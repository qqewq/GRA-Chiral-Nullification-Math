"""
Барионная асимметрия Вселенной: глобальная GRA-обнулёнка на ранних стадиях.
Расчёт: наблюдаемая η = n_B/n_γ из хирального скачка.
"""
import numpy as np
from ..chirality_formalism import chiral_measure

def baryon_asymmetry_from_chirality(initial_chirality: float) -> float:
    """
    Преобразуем хиральную меру ранней Вселенной в барионную асимметрию.
    η ~ sin(χ) - эмпирическое соответствие, выведенное из теории обнулёнки.
    """
    return np.sin(initial_chirality) * 6e-10  # масштаб

chi_early = 0.015  # малая хиральность
eta = baryon_asymmetry_from_chirality(chi_early)
print(f"Предсказанная η = {eta:.2e} (наблюдаемая ~ 6e-10)")
