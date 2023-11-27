import pytest
from rayTracer.planes import Planes
from rayTracer.tuples import Tuples
from rayTracer.rays import Rays


def test_plane_normal():
    p = Planes()
    n1 = p.local_normal_at(Tuples().Point(0, 0, 0))
    n2 = p.local_normal_at(Tuples().Point(10, 0, -10))
    n3 = p.local_normal_at(Tuples().Point(-5, 0, 150))
    assert n1 == Tuples().Vector(0,1,0)
    assert n2 == Tuples().Vector(0,1,0)
    assert n3 == Tuples().Vector(0,1,0)
    
def test_intersect_parallel_ray():
    p = Planes()
    r = Rays(Tuples().Point(0, 10, 0), Tuples().Vector(0, 0, 1))
    xs = p.local_intersect(r)
    assert len(xs) == 0
    
def test_intersect_coplanar_ray():
    p = Planes()
    r = Rays(Tuples().Point(0, 0, 0), Tuples().Vector(0, 0, 1))
    xs = p.local_intersect(r)
    assert len(xs) == 0
    
def test_interesct_above():
    p = Planes()
    r = Rays(Tuples().Point(0, 1, 0), Tuples().Vector(0, -1, 0))
    xs = p.local_intersect(r)
    assert len(xs) == 1
    assert xs[0].t == 1
    assert xs[0].obj == p
    
def test_intersect_below():
    p = Planes()
    r = Rays(Tuples().Point(0, -1, 0), Tuples().Vector(0, 1, 0))
    xs = p.local_intersect(r)
    assert len(xs) == 1
    assert xs[0].t == 1
    assert xs[0].obj == p
    