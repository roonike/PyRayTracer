import pytest
from rayTracer.shapes import Shapes
from rayTracer.transformations import Transformations
from rayTracer.matrix import Matrix
from rayTracer.materials import Materials
from rayTracer.tuples import Tuples
from rayTracer.rays import Rays


def test_default_shape():
    shape = Shapes()
    assert shape.transform == Matrix(4,4).identity()
    
def test_transform_assign():
    shape = Shapes()
    shape.set_transform(Transformations.translation(2,3,4))
    assert shape.transform == Transformations.translation(2,3,4)
    
def test_default_material():
    shape = Shapes()
    m = Materials()
    assert shape.material == m

def test_assign_material():
    shape = Shapes()
    m = Materials()
    m.ambient = 1
    shape.material = m
    assert shape.material == m

def test_intersecting_scaled_shape():
    origin = Tuples().Point(0, 0, -5)
    direction = Tuples().Vector(0, 0, 1)
    ray = Rays(origin, direction)
    trans = Transformations()
    scaling = trans.scaling(2, 2, 2)
    shape = Shapes()
    shape = shape.set_transform(scaling)
    intersections = shape.intersect(ray)
    assert shape.saved_ray.origin == Tuples().Point(0,0,-2.5)
    assert shape.saved_ray.direction == Tuples().Vector(0,0,0.5)


def test_intersecting_translated_shape():
    origin = Tuples().Point(0, 0, -5)
    direction = Tuples().Vector(0, 0, 1)
    ray = Rays(origin, direction)
    trans = Transformations()
    translation = trans.translation(5, 0, 0)
    shape = Shapes()
    shape = shape.set_transform(translation)
    intersections = shape.intersect(ray)
    print(shape.saved_ray.origin)
    print(shape.saved_ray.direction)
    assert shape.saved_ray.origin == Tuples().Point(-5,0,-5)
    assert shape.saved_ray.direction == Tuples().Vector(0,0,1)
    
def test_normal_translated_shape():
    trans = Transformations()
    shape = Shapes()
    shape.set_transform(trans.translation(0, 1, 0))
    Point = Tuples().Point(0, 1.70711, -0.70711)
    expected = Tuples().Vector(0, 0.70711, -0.70711)
    normal = shape.normal_at(Point)
    print(expected,normal)
    assert normal == expected

def test_normal_transformed_shape():
    trans = Transformations()
    shape = Shapes()
    m = trans.scaling(1, 0.5, 1) * trans.rotation_z(3.14159/5)
    shape.set_transform(m)
    Point = Tuples().Point(0, (2 ** 0.5) / 2, -(2 ** 0.5) / 2)
    expected = Tuples().Vector(0, 0.97014, -0.24254)
    normal = shape.normal_at(Point)
    print(expected,normal)
    assert normal == expected
