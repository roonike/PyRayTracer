from rayTracer.sphere import Sphere
from rayTracer.intersection import Intersection
from rayTracer.computations import Computations
from rayTracer.tuples import Tuples
from rayTracer.rays import Rays
from rayTracer.transformations import Transformations

EPSILON = 0.00001

def test_intersection_encapsulates_t():
    s1 = Sphere()
    inter = Intersection(3.5, s1)
    assert inter.obj.id == s1.id
    assert inter.t == 3.5

def test_aggregating_intersections():
    s = Sphere()
    i1 = Intersection(1, s)
    i2 = Intersection(2, s)
    xs = Intersection.intersections(i1, i2)
    print(str(xs))
    assert len(xs) == 2
    assert xs[0].t == 1
    assert xs[1].t == 2

def test_hit_positive_t():
    s = Sphere()
    i1 = Intersection(1, s)
    i2 = Intersection(2, s)
    xs = Intersection.intersections(i1, i2)
    result = i1.hit(xs)
    assert result == i1

def test_hit_positive_negative_t():
    s = Sphere()
    i1 = Intersection(-1.0, s)
    i2 = Intersection(1, s)
    xs = Intersection.intersections(i1, i2)
    result = i1.hit(xs)
    assert result == i2

def test_hit_negative_t():
    s = Sphere()
    i1 = Intersection(-2, s)
    i2 = Intersection(-1, s)
    xs = Intersection.intersections(i1, i2)
    result = i1.hit(xs)
    assert result is None

def test_lowest_nonnegative():
    s = Sphere()
    i1 = Intersection(5, s)
    i2 = Intersection(7, s)
    i3 = Intersection(-3, s)
    i4 = Intersection(2, s)
    xs = Intersection.intersections(i1, i2, i3, i4)
    result = i1.hit(xs)
    assert result == i4

def test_precomputing_state():
    shape = Sphere()
    origin = Tuples().Point(0, 0, -5)
    direction = Tuples().Vector(0, 0, 1)
    r = Rays(origin, direction)
    i = Intersection(4, shape)
    c = Computations()
    comps = c.prepare_computations(i, r)
    pointR = Tuples().Point(0, 0, -1)
    vectorR = Tuples().Vector(0, 0, -1)
    assert comps.t == i.t
    assert comps.object == i.obj
    assert comps.point == pointR
    assert comps.eyev == vectorR
    assert comps.normalv == vectorR

def test_hit_intersection_outside():
    shape = Sphere()
    origin = Tuples().Point(0, 0, -5)
    direction = Tuples().Vector(0, 0, 1)
    r = Rays(origin, direction)
    i = Intersection(4, shape)
    c = Computations()
    comps = c.prepare_computations(i, r)
    assert not comps.inside

def test_hit_intersection_inside():
    shape = Sphere()
    origin = Tuples().Point(0, 0, 0)
    direction = Tuples().Vector(0, 0, 1)
    r = Rays(origin, direction)
    i = Intersection(1, shape)
    c = Computations()
    comps = c.prepare_computations(i, r)
    pointR = Tuples().Point(0, 0, 1)
    vectorR = Tuples().Vector(0, 0, -1)
    assert comps.inside
    assert comps.point == pointR
    assert comps.eyev == vectorR
    assert comps.normalv == vectorR
    
def test_hit_should_offset_point():
    r = Rays(Tuples().Point(0, 0, -5), Tuples().Vector(0, 0, 1))
    shape = Sphere()
    shape.transform = Transformations().translation(0, 0, 1)
    i = Intersection(5, shape)
    comps = Computations().prepare_computations(i, r)
    assert comps.over_point.z < -EPSILON/2
    assert comps.point.z > comps.over_point.z
