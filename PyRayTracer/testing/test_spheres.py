import pytest
from rayTracer.rays import Rays
from rayTracer.sphere import Sphere
from rayTracer.intersection import Intersection
from rayTracer.transformations import Transformations
from rayTracer.tuples import Tuples
from rayTracer.materials import Materials
from rayTracer.matrix import Matrix

def test_two_points_intersection_sphere():
    origin = Tuples().Point(0, 0, -5)
    direction = Tuples().Vector(0, 0, 1)
    ray = Rays(origin, direction)
    sphere = Sphere()
    intersections = Intersection().intersect(sphere, ray)
    print(str(intersections[0].t))
    print(str(intersections[1].t))
    assert len(intersections) == 2
    assert intersections[0].t == 4.0
    assert intersections[1].t == 6.0


def test_one_point_tangent_sphere():
    origin = Tuples().Point(0, 1, -5)
    direction = Tuples().Vector(0, 0, 1)
    ray = Rays(origin, direction)
    sphere = Sphere()
    intersections = Intersection().intersect(sphere, ray)
    assert len(intersections) == 2
    assert intersections[0].t == 5.0
    assert intersections[1].t == 5.0

def test_ray_misses_sphere():
    origin = Tuples().Point(0, 2, -5)
    direction = Tuples().Vector(0, 0, 1)
    ray = Rays(origin, direction)
    sphere = Sphere()
    intersections = Intersection().intersect(sphere, ray)
    assert len(intersections) == 0

def test_ray_originates_inside_sphere():
    origin = Tuples().Point(0, 0, 0)
    direction = Tuples().Vector(0, 0, 1)
    ray = Rays(origin, direction)
    sphere = Sphere()
    intersections = Intersection().intersect(sphere, ray)
    assert len(intersections) == 2
    assert intersections[0].t == -1.0
    assert intersections[1].t == 1.0

def test_sphere_behind_ray():
    origin = Tuples().Point(0, 0, 5)
    direction = Tuples().Vector(0, 0, 1)
    ray = Rays(origin, direction)
    sphere = Sphere()
    intersections = Intersection().intersect(sphere, ray)
    assert len(intersections) == 2
    assert intersections[0].t == -6.0
    assert intersections[1].t == -4.0

def test_object_on_intersection():
    origin = Tuples().Point(0, 0, -5)
    direction = Tuples().Vector(0, 0, 1)
    ray = Rays(origin, direction)
    sphere = Sphere()
    intersections = Intersection().intersect(sphere, ray)
    assert len(intersections) == 2
    assert intersections[0].obj.id == sphere.id
    assert intersections[1].obj.id == sphere.id

def test_default_transformation():
    sphere = Sphere()
    compare = sphere.transform
    ident = Matrix(4,4).identity()
    expected = ident
    assert compare == expected

def test_changing_transformation():
    trans = Transformations()
    sphere = Sphere()
    translation = trans.translation(2, 3, 4)
    sphere = sphere.set_transform(translation)
    expected = translation
    assert sphere.transform == expected

def test_intersecting_scaled_sphere():
    origin = Tuples().Point(0, 0, -5)
    direction = Tuples().Vector(0, 0, 1)
    ray = Rays(origin, direction)
    trans = Transformations()
    scaling = trans.scaling(2, 2, 2)
    sphere = Sphere()
    sphere = sphere.set_transform(scaling)
    intersections = Intersection().intersect(sphere, ray)
    assert len(intersections) == 2
    assert intersections[0].t == 3
    assert intersections[1].t == 7

def test_intersecting_translated_sphere():
    origin = Tuples().Point(0, 0, -5)
    direction = Tuples().Vector(0, 0, 1)
    ray = Rays(origin, direction)
    trans = Transformations()
    translation = trans.translation(5, 0, 0)
    sphere = Sphere()
    sphere = sphere.set_transform(translation)
    intersections = Intersection().intersect(sphere, ray)
    assert len(intersections) == 0

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

def test_normal_translated_sphere():
    trans = Transformations()
    sphere = Sphere()
    sphere.set_transform(trans.translation(0, 1, 0))
    Point = Tuples().Point(0, 1.70711, -0.70711)
    expected = Tuples().Vector(0, 0.70711, -0.70711)
    normal = sphere.normal_at(Point)
    assert normal == expected

def test_normal_transformed_sphere():
    trans = Transformations()
    sphere = Sphere()
    m = trans.scaling(1, 0.5, 1) * trans.rotation_z(3.14159/5)
    sphere.set_transform(m)
    Point = Tuples().Point(0, (2 ** 0.5) / 2, -(2 ** 0.5) / 2)
    expected = Tuples().Vector(0, 0.97014, -0.24254)
    normal = sphere.normal_at(Point)
    assert normal == expected

def test_sphere_default_material():
    sphere = Sphere()
    m = sphere.material
    expected = Materials()
    assert m == expected

def test_sphere_assigned_material():
    sphere = Sphere()
    m = Materials()
    m.ambient = 1
    sphere.material = m
    assert m == sphere.material
