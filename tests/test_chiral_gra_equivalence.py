import numpy as np
from gra_chiral_null import mirror_operator_nd, gra_null_as_chiral

def test_chiral_null_equivalence():
    Z = mirror_operator_nd(0)
    x = np.array([1,2,3])
    w = {"a":1}
    s = {}
    res = gra_null_as_chiral(x, w, s, Z)
    R, L = res.policy
    assert np.array_equal(R, x)
    assert np.array_equal(L, Z(x))
    assert res.weights == {"a":0.0}
    assert res.state is None
