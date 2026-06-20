"""
Политическая хиральность: левые/правые идеологии как зеркальные пары.
"""
from ..chirality_formalism import chiral_pair

def political_spectrum(ideology_vector: np.ndarray, Z):
    """Идеология и её антипод."""
    return chiral_pair(ideology_vector, Z)

Z_politics = lambda v: -v  # полное отражение
ideology = np.array([0.7, -0.2])  # координаты "свобода-равенство"
left, right = political_spectrum(ideology, Z_politics)
print("Правый вектор:", left, "Левый вектор:", right)
