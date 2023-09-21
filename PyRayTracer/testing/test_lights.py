import pytest
from rayTracer.lights import PointLight
from rayTracer.tuples import Tuple, Color

def test_point_light_with_intensity_position():
    intensity = Color(1, 1, 1)
    position = Tuple.point(0, 0, 0)
    light = PointLight(position, intensity)
    assert light.position == position
    assert light.intensity == intensity


