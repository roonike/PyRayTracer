import pytest
from rayTracer.rays import Ray
from rayTracer.tuples import Tuple
from rayTracer.transformations import Transformation
from rayTracer.intersection import Intersection

def test_create_ray():
    origin = Tuple.point(1, 2, 3)
    direction = Tuple.vector(4, 5, 6)
    ray = Ray(origin, direction)
    assert ray.origin == origin
    assert ray.direction == direction

def test_compute_point_distance():
    origin = Tuple.point(2, 3, 4)
    direction = Tuple.vector(1, 0, 0)
    ray = Ray(origin, direction)
    expected1 = Tuple.point(2, 3, 4)
    expected2 = Tuple.point(3, 3, 4)
    expected3 = Tuple.point(1, 3, 4)
    expected4 = Tuple.point(4.5, 3, 4)
    assert ray.position(0) == expected1
    assert ray.position(1) == expected2
    assert ray.position(-1) == expected3
    assert ray.position(2.5) == expected4

def test_translating_ray():
    origin = Tuple.point(1, 2, 3)
    direction = Tuple.vector(0, 1, 0)
    ray = Ray(origin, direction)
    trans = Transformation.translation(3, 4, 5)
    expected_origin = Tuple.point(4, 6, 8)
    expected_direction = Tuple.vector(0, 1, 0)
    transformed_ray = Intersection.transform(ray, trans)
    assert transformed_ray.origin == expected_origin
    assert transformed_ray.direction == expected_direction

def test_scaling_ray():
    origin = Tuple.point(1, 2, 3)
    direction = Tuple.vector(0, 1, 0)
    ray = Ray(origin, direction)
    trans = Transformation.scaling(2, 3, 4)
    expected_origin = Tuple.point(2, 6, 12)
    expected_direction = Tuple.vector(0, 3, 0)
    transformed_ray = Intersection.transform(ray, trans)
    assert transformed_ray.origin == expected_origin
    assert transformed_ray.direction == expected_direction