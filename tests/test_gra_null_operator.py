import numpy as np
from gra_chiral_null import gra_nullify, GRANullState, gra_null_as_chiral, mirror_operator_nd

def test_gra_nullify():
    def reparam(p):
        return p * 2
    res = gra_nullify(5, {"a": 1.0}, "active", reparam)
    assert res.policy == 10
    assert res.weights == {"a": 0.0}
    assert res.state is None

def test_gra_null_state_dataclass():
    s = GRANullState(policy="p", weights={"w": 0.0}, state=None)
    assert s.policy == "p"
    assert s.weights == {"w": 0.0}
