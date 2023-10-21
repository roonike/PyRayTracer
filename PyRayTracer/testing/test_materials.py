import pytest
from rayTracer.materials import Materials
from rayTracer.tuples import Tuples
from rayTracer.colors import Colors
from rayTracer.lights import Lights

def test_default_material():
    m = Materials()
    color = Colors(1, 1, 1)
    assert m.color == color
    assert m.ambient == 0.1
    assert m.diffuse == 0.9
    assert m.specular == 0.9
    assert m.shininess == 200.0

def test_eye_between_light_surface():
    m = Materials()
    position = Tuples()
    position = position.Point(0, 0, 0)
    eyev = Tuples()
    eyev = eyev.Vector(0, 0, -1)
    normalv = Tuples()
    normalv = normalv.Vector(0, 0, -1)
    intensity = Colors(1, 1, 1)
    light_position = Tuples()
    light_position = light_position.Point(0, 0, -10)
    light = Lights()
    light.point_light(light_position, intensity)
    expected_color = Colors(1.9, 1.9, 1.9)
    result = light.lighting(m, light, position, eyev, normalv)
    assert result == expected_color

def test_light_surface_eye_offset_45():
    m = Materials()
    position = Tuples()
    position = position.Point(0, 0, 0)
    eyev = Tuples()
    eyev = eyev.Vector(0, 2**0.5/2, 2**0.5/2)
    normalv = Tuples()
    normalv = normalv.Vector(0, 0, -1)
    intensity = Colors(1, 1, 1)
    light_position = Tuples()
    light_position = light_position.Point(0, 0, -10)
    light = Lights()
    light.point_light(light_position, intensity)
    expected_color = Colors(1.0, 1.0, 1.0)
    result = light.lighting(m, light, position, eyev, normalv)
    assert result == expected_color

def test_eye_surface_light_offset_45():
    m = Materials()
    position = Tuples()
    position = position.Point(0, 0, 0)
    eyev = Tuples()
    eyev = eyev.Vector(0, 0, -1)
    normalv = Tuples()
    normalv = normalv.Vector(0, 0, -1)
    intensity = Colors(1, 1, 1)
    light_position = Tuples()
    light_position = light_position.Point(0, 10, -10)
    light = Lights()
    light.point_light(light_position, intensity)
    expected_color = Colors(0.7364, 0.7364, 0.7364)
    result = light.lighting(m, light, position, eyev, normalv)
    assert result == expected_color

def test_eye_in_path_of_reflection_vector():
    m = Materials()
    position = Tuples()
    position = position.Point(0, 0, 0)
    eyev = Tuples()
    eyev = eyev.Vector(0, -2**0.5/2, -2**0.5/2)
    normalv = Tuples()
    normalv = normalv.Vector(0, 0, -1)
    intensity = Colors(1, 1, 1)
    light_position = Tuples()
    light_position = light_position.Point(0, 10, -10)
    light = Lights()
    light.point_light(light_position, intensity)
    expected_color = Colors(1.6364, 1.6364, 1.6364)
    result = light.lighting(m, light, position, eyev, normalv)
    assert result == expected_color

def test_light_behind_the_surface():
    m = Materials()
    position = Tuples()
    position = position.Point(0, 0, 0)
    eyev = Tuples()
    eyev = eyev.Vector(0, 0, -1)
    normalv = Tuples()
    normalv = normalv.Vector(0, 0, -1)
    intensity = Colors(1, 1, 1)
    light_position = Tuples()
    light_position = light_position.Point(0, 0, 10)
    light = Lights()
    light.point_light(light_position, intensity)
    expected_color = Colors(0.1, 0.1, 0.1)
    result = light.lighting(m, light, position, eyev, normalv)
    assert result == expected_color

def test_lighting_surface_in_shadow():
    m = Materials()
    position = Tuples()
    position = position.Point(0, 0, 0)
    eyev = Tuples().Vector(0, 0, -1)
    normalv = Tuples().Vector(0, 0, -1)
    light = Lights()
    light.point_light(Tuples().Point(0, 0, -10), Colors(1,1,1))
    in_shadow = True
    result = light.lighting(m, light, position, eyev, normalv, in_shadow)
    assert result == Colors(0.1, 0.1, 0.1)
    