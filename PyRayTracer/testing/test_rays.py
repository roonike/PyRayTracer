import pytest
from rayTracer.rays import Rays
from rayTracer.tuples import Tuples
from rayTracer.transformations import Transformations
from rayTracer.intersection import Intersection

def test_create_ray():
    origin = Tuples().Point(1, 2, 3)
    direction = Tuples().Vector(4, 5, 6)
    ray = Rays(origin, direction)
    assert ray.origin == origin
    assert ray.direction == direction

def test_compute_point_distance():
    origin = Tuples().Point(2, 3, 4)
    direction = Tuples().Vector(1, 0, 0)
    ray = Rays(origin, direction)
    expected1 = Tuples().Point(2, 3, 4)
    expected2 = Tuples().Point(3, 3, 4)
    expected3 = Tuples().Point(1, 3, 4)
    expected4 = Tuples().Point(4.5, 3, 4)
    assert ray.position(0) == expected1
    assert ray.position(1) == expected2
    assert ray.position(-1) == expected3
    assert ray.position(2.5) == expected4

def test_translating_ray():
    origin = Tuples().Point(1, 2, 3)
    direction = Tuples().Vector(0, 1, 0)
    ray = Rays(origin, direction)
    trans = Transformations().translation(3, 4, 5)
    expected_origin = Tuples().Point(4, 6, 8)
    expected_direction = Tuples().Vector(0, 1, 0)
    transformed_ray = Intersection().transform(ray, trans)
    assert transformed_ray.origin == expected_origin
    assert transformed_ray.direction == expected_direction

def test_scaling_ray():
    origin = Tuples().Point(1, 2, 3)
    direction = Tuples().Vector(0, 1, 0)
    ray = Rays(origin, direction)
    trans = Transformations().scaling(2, 3, 4)
    expected_origin = Tuples().Point(2, 6, 12)
    expected_direction = Tuples().Vector(0, 3, 0)
    transformed_ray = Intersection().transform(ray, trans)
    assert transformed_ray.origin == expected_origin
    assert transformed_ray.direction == expected_direction