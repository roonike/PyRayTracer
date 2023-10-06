import pytest
from rayTracer.lights import Lights
from rayTracer.tuples import Tuples
from rayTracer.colors import Colors

def test_point_light_with_intensity_position():
    intensity = Colors(1, 1, 1)
    position = Tuples()
    position = position.Point(0, 0, 0)
    light = Lights()
    light.point_light(position, intensity)
    assert light.position == position
    assert light.intensity == intensity


