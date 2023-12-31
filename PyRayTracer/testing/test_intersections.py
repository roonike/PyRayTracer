from rayTracer.sphere import Sphere
from rayTracer.intersection import Intersection
from rayTracer.computations import Computations
from rayTracer.tuples import Tuples
from rayTracer.rays import Rays
from rayTracer.transformations import Transformations
from rayTracer.planes import Planes
from math import sqrt

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

def test_precompute_reflect_vector():
    shape = Planes()
    r = Rays(Tuples().Point(0,1,-1),Tuples().Vector(0,-sqrt(2)/2,sqrt(2)/2))
    i = Intersection(sqrt(2),shape)
    comps = Computations().prepare_computations(i,r)
    assert comps.reflectv == Tuples().Vector(0,sqrt(2)/2,sqrt(2)/2)
    
def test_find_n1_n2_at_mult_intersect():
    a = Sphere().glass()
    a.transform = Transformations().scaling(2,2,2)
    a.material.refractive_index = 1.5
    b = Sphere().glass()
    b.transform = Transformations().translation(0,0,-.25)
    b.material.refractive_index = 2.0
    c = Sphere().glass()
    c.transform = Transformations().translation(0,0,.25)
    c.material.refractive_index = 2.5
    r = Rays(Tuples().Point(0,0,-4) , Tuples().Vector(0,0,1))
    x1 = Intersection(2,a)
    x2 = Intersection(2.75,b)
    x3 = Intersection(3.25,c)
    x4 = Intersection(4.75,b)
    x5 = Intersection(5.25,c)
    x6 = Intersection(6,a)
    xs = Intersection().intersections(x1,x2,x3,x4,x5,x6)
    comps = Computations().prepare_computations(xs[0],r,xs)
    assert comps.n1 == 1.0
    assert comps.n2 == 1.5
    comps = Computations().prepare_computations(xs[1],r,xs)
    assert comps.n1 == 1.5
    assert comps.n2 == 2.0
    comps = Computations().prepare_computations(xs[2],r,xs)
    assert comps.n1 == 2.0
    assert comps.n2 == 2.5
    comps = Computations().prepare_computations(xs[3],r,xs)
    assert comps.n1 == 2.5
    assert comps.n2 == 2.5
    comps = Computations().prepare_computations(xs[4],r,xs)
    assert comps.n1 == 2.5
    assert comps.n2 == 1.5
    comps = Computations().prepare_computations(xs[5],r,xs)
    assert comps.n1 == 1.5
    assert comps.n2 == 1.0
    
def test_under_point():
    r = Rays(Tuples().Point(0,0,-5),Tuples().Vector(0,0,1))
    shape = Sphere().glass()
    shape.transform = Transformations.translation(0,0,1)
    i = Intersection(5,shape)
    xs = Intersection.intersections(i)
    comps = Computations().prepare_computations(i,r,xs)
    
    assert comps.under_point.z > EPSILON/2
    assert comps.point.z < comps.under_point.z
    
def test_schlick_under_total_internal_reflection():
    shape = Sphere().glass()
    r = Rays(Tuples().Point(0,0,sqrt(2)/2),Tuples().Vector(0,1,0))
    xs = Intersection.intersections(Intersection(-sqrt(2)/2,shape),Intersection(sqrt(2)/2,shape))
    comps = Computations().prepare_computations(xs[1],r,xs)
    reflectance = comps.schlick()
    assert reflectance == 1.0
    
def test_schlick_perpendicular():
    shape = Sphere().glass()
    r = Rays(Tuples().Point(0,0,0), Tuples().Vector(0,1,0))
    xs =Intersection.intersections(Intersection(-1,shape),Intersection(1,shape))
    comps = Computations().prepare_computations(xs[1],r,xs)
    reflectance = comps.schlick()
    assert reflectance == 0.04
    
def test_schlick_n2_greater_than_n1():
    shape = Sphere().glass()
    r = Rays(Tuples().Point(0,0.99,-2), Tuples().Vector(0,0,1))
    xs = Intersection.intersections(Intersection(1.8589,shape))
    comps = Computations().prepare_computations(xs[0],r,xs)
    reflectance = comps.schlick()
    assert reflectance == 0.48873