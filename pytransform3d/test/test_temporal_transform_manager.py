import numpy as np
from numpy.testing import assert_array_almost_equal

from pytransform3d.transform_manager import (
    TemporalTransformManager, StaticTransform)
from pytransform3d.transformations import random_transform, invert_transform


def test_temporal_transform():
    rng = np.random.default_rng(0)
    A2B = random_transform(rng)

    rng = np.random.default_rng(42)
    A2C = random_transform(rng)

    tm = TemporalTransformManager()

    tm.add_transform("A", "B", StaticTransform(A2B))
    tm.add_transform("A", "C", StaticTransform(A2C))

    tm.current_time = 1234.0
    B2C = tm.get_transform("B", "C")

    C2B = tm.get_transform("C", "B")
    B2C_2 = invert_transform(C2B)
    assert_array_almost_equal(B2C, B2C_2)

    B2C_3 = tm.get_transform_at_time("B", "C", 1234.0)
    assert_array_almost_equal(B2C_2, B2C_3)


def test_internals():
    rng = np.random.default_rng(0)
    A2B = random_transform(rng)

    rng = np.random.default_rng(42)
    A2C = random_transform(rng)

    tm = TemporalTransformManager()

    tm.add_transform("A", "B", StaticTransform(A2B))
    tm.add_transform("A", "C", StaticTransform(A2C))

    tm.remove_transform("A", "C")
    assert ("A", "C") not in tm.transforms