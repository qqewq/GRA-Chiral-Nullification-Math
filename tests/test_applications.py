import numpy as np
from gra_chiral_null.applications.physics import cp_violation_parameter
from gra_chiral_null.applications.chemistry import enantiomeric_excess
from gra_chiral_null.applications.cosmology import baryon_asymmetry_from_chirality

def test_cp_violation():
    state = np.array([1.0 + 0.01j, 0.0])
    eps = cp_violation_parameter(state)
    assert 0 <= eps < 1

def test_enantiomeric_excess():
    cat = np.array([0.8, 0.2])
    ee = enantiomeric_excess(cat)
    assert 0 <= ee <= 1

def test_baryon_asymmetry():
    eta = baryon_asymmetry_from_chirality(0.015)
    assert eta > 0
    assert eta < 1e-9
