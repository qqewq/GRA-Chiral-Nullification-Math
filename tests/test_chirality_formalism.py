import numpy as np
from gra_chiral_null import mirror_operator_nd, chiral_pair, is_chiral, chiral_measure
from gra_chiral_null.metrics_and_examples import euclidean_metric, generate_rotations_2d

def test_mirror_operator():
    Z = mirror_operator_nd(0)
    x = np.array([1, 2, 3])
    zx = Z(x)
    assert zx[0] == -1
    assert zx[1] == 2
    assert zx[2] == 3

def test_chiral_pair():
    Z = mirror_operator_nd(1)
    x = np.array([1.0, 2.0])
    R, L = chiral_pair(x, Z)
    assert np.array_equal(R, x)
    assert np.array_equal(L, np.array([1.0, -2.0]))

def test_is_chiral():
    Z = mirror_operator_nd(0)
    x = np.array([1.0, 0.0])
    rotations = generate_rotations_2d(8)
    assert is_chiral(x, Z, rotations)

def test_chiral_measure():
    Z = mirror_operator_nd(0)
    x = np.array([3.0, 0.0])
    chi = chiral_measure(x, Z, euclidean_metric)
    assert chi == 6.0
