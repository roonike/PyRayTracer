import pytest
from rayTracer.rays import Rays
from rayTracer.sphere import Sphere
from rayTracer.transformations import Transformations
from rayTracer.tuples import Tuples
from rayTracer.materials import Materials
from rayTracer.matrix import Matrix

def test_two_points_intersection_sphere():
    origin = Tuples().Point(0, 0, -5)
    direction = Tuples().Vector(0, 0, 1)
    ray = Rays(origin, direction)
    sphere = Sphere()
    intersections = sphere.local_intersect(ray)
    assert len(intersections) == 2
    assert intersections[0].t == 4.0
    assert intersections[1].t == 6.0

def test_one_point_tangent_sphere():
    origin = Tuples().Point(0, 1, -5)
    direction = Tuples().Vector(0, 0, 1)
    ray = Rays(origin, direction)
    sphere = Sphere()
    intersections = sphere.local_intersect(ray)
    assert len(intersections) == 2
    assert intersections[0].t == 5.0
    assert intersections[1].t == 5.0

def test_ray_misses_sphere():
    origin = Tuples().Point(0, 2, -5)
    direction = Tuples().Vector(0, 0, 1)
    ray = Rays(origin, direction)
    sphere = Sphere()
    intersections = sphere.local_intersect(ray)
    assert len(intersections) == 0

def test_ray_originates_inside_sphere():
    origin = Tuples().Point(0, 0, 0)
    direction = Tuples().Vector(0, 0, 1)
    ray = Rays(origin, direction)
    sphere = Sphere()
    intersections = sphere.local_intersect(ray)
    assert len(intersections) == 2
    assert intersections[0].t == -1.0
    assert intersections[1].t == 1.0

def test_sphere_behind_ray():
    origin = Tuples().Point(0, 0, 5)
    direction = Tuples().Vector(0, 0, 1)
    ray = Rays(origin, direction)
    sphere = Sphere()
    intersections = sphere.local_intersect(ray)
    assert len(intersections) == 2
    assert intersections[0].t == -6.0
    assert intersections[1].t == -4.0

def test_object_on_intersection():
    origin = Tuples().Point(0, 0, -5)
    direction = Tuples().Vector(0, 0, 1)
    ray = Rays(origin, direction)
    sphere = Sphere()
    intersections = sphere.local_intersect(ray)
    assert len(intersections) == 2
    assert intersections[0].obj.id == sphere.id
    assert intersections[1].obj.id == sphere.id

def test_normal_sphere_x_axis():
    sphere = Sphere()
    Point = Tuples().Point(1, 0, 0)
    expected = Tuples().Vector(1, 0, 0)
    normal = sphere.normal_at(Point)
    assert normal == expected


def test_normal_sphere_y_axis():
    sphere = Sphere()
    Point = Tuples().Point(0, 1, 0)
    expected = Tuples().Vector(0, 1, 0)
    normal = sphere.normal_at(Point)
    assert normal == expected

def test_normal_sphere_z_axis():
    sphere = Sphere()
    Point = Tuples().Point(0, 0, 1)
    expected = Tuples().Vector(0, 0, 1)
    normal = sphere.normal_at(Point)
    assert normal == expected

def test_normal_sphere_non_axial():
    sphere = Sphere()
    Point = Tuples().Point((3 ** 0.5) / 3, (3 ** 0.5) / 3, (3 ** 0.5) / 3)
    expected = Tuples().Vector((3 ** 0.5) / 3, (3 ** 0.5) / 3, (3 ** 0.5) / 3)
    normal = sphere.normal_at(Point)
    assert normal == expected

def test_normal_normalized_vector():
    sphere = Sphere()
    Point = Tuples().Point((3 ** 0.5) / 3, (3 ** 0.5) / 3, (3 ** 0.5) / 3)
    normal = sphere.normal_at(Point)
    assert normal == normal.normalize()
    
def test_glass_sphere():
    s = Sphere().glass()
    assert s.transform == Matrix(4,4).identity()
    assert s.material.transparency == 1.0
    assert s.material.refractive_index == 1.5