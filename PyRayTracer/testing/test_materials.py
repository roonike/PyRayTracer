import pytest
from rayTracer.materials import Materials
from rayTracer.tuples import Tuples
from rayTracer.colors import Colors
from rayTracer.lights import Lights
from rayTracer.stripes import Stripes
from rayTracer.sphere import Sphere
from math import floor

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
    result = light.lighting(m,Sphere(), light, position, eyev, normalv, False)
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
    result = light.lighting(m,Sphere(), light, position, eyev, normalv, False)
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
    result = light.lighting(m,Sphere(), light, position, eyev, normalv, False)
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
    result = light.lighting(m,Sphere(), light, position, eyev, normalv, False)
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
    result = light.lighting(m,Sphere(), light, position, eyev, normalv, False)
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
    result = light.lighting(m,Sphere(), light, position, eyev, normalv, in_shadow)
    assert result == Colors(0.1, 0.1, 0.1)
    
def test_lighting_with_pattern():
    m = Materials()
    m.pattern = Stripes().pattern(Colors(1,1,1),Colors(0,0,0))
    m.ambient = 1
    m.diffuse = 0
    m.specular = 0
    eyev = Tuples().Vector(0,0,-1)
    normalv = Tuples().Vector(0,0,-1)
    light = Lights(Tuples().Point(0,0,-10),Colors(1,1,1))
    point1 = Tuples().Point(0.9,0,0)
    point2 = Tuples().Point(1.1,0,0)
    c1 = light.lighting(m,Sphere(),light,point1,eyev,normalv,False)
    c2 = light.lighting(m,Sphere(),light,point2,eyev,normalv,False)
    assert c1 == Colors(1,1,1)
    assert c2 == Colors(0,0,0)
    
def test_default_reflect():
    m = Materials()
    assert m.reflective == 0.0

def test_default_refraction_transparency():
    m = Materials()
    assert m.transparency == 0.0
    assert m.refractive_index == 1.0