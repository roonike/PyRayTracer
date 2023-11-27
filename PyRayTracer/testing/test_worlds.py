import pytest
from math import sqrt
from rayTracer.worlds import World
from rayTracer.rays import Rays
from rayTracer.sphere import Sphere
from rayTracer.intersection import Intersection
from rayTracer.computations import Computations
from rayTracer.tuples import Tuples
from rayTracer.colors import Colors
from rayTracer.lights import Lights
from rayTracer.materials import Materials
from rayTracer.transformations import Transformations
from rayTracer.planes import Planes
from rayTracer.patterns import Patterns

def test_creating_world():
    world = World()
    assert len(world.objects) == 0

def test_creating_default_world():
    world = World()
    world.default_world()

    light = Lights()
    point = Tuples().Point(-10, 10, -10)
    color = Colors(1, 1, 1)
    light.point_light(point, color)

    material = Materials()
    material_color = Colors(0.8, 1.0, 0.6)
    material.color = material_color
    material.diffuse = 0.7
    material.specular = 0.2

    s1 = Sphere()
    s1.material = material

    trans = Transformations()
    s2 = Sphere()
    s2.set_transform(trans.scaling(0.5, 0.5, 0.5))
    
    print(light.intensity)
    print(light.position)
    print(world.light.intensity)
    print(world.light.position)

    assert world.light == light
    assert s1 in world.objects
    assert s2 in world.objects



def test_intersect_world_ray():
    world = World()
    world.default_world()

    origin = Tuples().Point(0, 0, -5)
    direction = Tuples().Vector(0, 0, 1)
    ray = Rays(origin, direction)

    inter = Intersection()
    xs = inter.intersect_world(world, ray)

    assert len(xs) == 4
    assert xs[0].t == 4
    assert xs[1].t == 4.5
    assert xs[2].t == 5.5
    assert xs[3].t == 6


def test_shading_intersection():
    world = World()
    world.default_world()

    origin = Tuples().Point(0, 0, -5)
    direction = Tuples().Vector(0, 0, 1)
    ray = Rays(origin, direction)

    shape = world.objects[0]

    i = Intersection(4, shape)
    com = Computations()
    comps = com.prepare_computations(i, ray)
    sphere = Sphere()
    c = com.shade_hit(world, comps)
    col = Colors(0.38066, 0.47583, 0.2855)
    assert c == col
    

def test_shading_intersection_inside():
    world = World()
    world.default_world()

    l = Lights()
    point = Tuples().Point(0, 0.25, 0)
    color = Colors(1, 1, 1)
    l.point_light(point, color)
    world.light = l

    origin = Tuples().Point(0, 0, 0)
    direction = Tuples().Vector(0, 0, 1)
    ray = Rays(origin, direction)

    shape = world.objects[1]

    i = Intersection(0.5, shape)
    com = Computations()
    comps = com.prepare_computations(i, ray)
    sphere = Sphere()
    c = com.shade_hit(world, comps)
    col = Colors(0.90498, 0.90498, 0.90498)
    print(c,col)
    assert c == col


def test_color_ray_misses():
    world = World()
    world.default_world()

    origin = Tuples().Point(0, 0, -5)
    direction = Tuples().Vector(0, 1, 0)
    ray = Rays(origin, direction)

    com = Computations()
    c = com.color_at(world, ray)
    col = Colors(0, 0, 0)

    assert c == col
    

def test_color_ray_hits():
    world = World()
    world.default_world()

    origin = Tuples().Point(0, 0, -5)
    direction = Tuples().Vector(0, 0, 1)
    ray = Rays(origin, direction)

    com = Computations()
    c = com.color_at(world, ray)
    col = Colors(0.38066, 0.47583, 0.2855)

    assert c == col

def test_color_intersection_behind_ray():
    world = World()
    world.default_world()

    outer = world.objects[0]
    outer.material.ambient = 1

    inner = world.objects[1]
    inner.material.ambient = 1

    origin = Tuples().Point(0, 0, 0.75)
    direction = Tuples().Vector(0, 0, -1)
    ray = Rays(origin, direction)

    com = Computations()
    c = com.color_at(world, ray)
    print(c)
    assert c == inner.material.color

def test_no_shadow_nothing_collinear_with_point_light():
    world = World().default_world()
    p = Tuples().Point(0, 10, 0)
    assert not world.is_shadowed(p)
    
def test_shadow_with_object_between_point_light():
    world = World().default_world()
    p = Tuples().Point(10, -10, 10)
    assert world.is_shadowed(p)
  
def test_no_shadow_with_object_behind_light():
    world = World().default_world()
    p = Tuples().Point(-20, 20, -20)
    assert not world.is_shadowed(p)
    
def test_no_shadow_with_object_behind_point():
    world = World().default_world()
    p = Tuples().Point(-2, 2, -2)
    assert not world.is_shadowed(p)
    
def test_shade_hit_given_intersection_in_shadow():
    w = World()
    l = Lights()
    l.point_light(Tuples().Point(0, 0, -10), Colors(1, 1, 1))
    w.light = l
    s1 = Sphere()
    w.objects.append(s1)
    s2 = Sphere()
    s2.transform = Transformations.translation(0, 0, 10)
    w.objects.append(s2)
    r = Rays(Tuples().Point(0, 0, 5), Tuples().Vector(0, 0, 1))
    i = Intersection(4, s2)
    comps = Computations().prepare_computations(i, r)
    sphere = Sphere()
    c = comps.shade_hit(w,comps)
    assert c == Colors(0.1, 0.1, 0.1)
    
def test_color_reflect_nonreflective():
    w = World().default_world()
    r = Rays(Tuples().Point(0,0,0),Tuples().Vector(0,0,1))
    shape = w.objects[1]
    shape.material.ambient = 1
    i = Intersection(1,shape)
    comps = Computations().prepare_computations(i,r)
    color = w.reflected_color(comps)
    assert color == Colors(0,0,0)
    
def test_color_reflect_reflective():
    w = World().default_world()
    shape = Planes()
    shape.material.reflective = 0.5
    shape.transform = Transformations.translation(0,-1,0)
    w.objects.append(shape)
    r = Rays(Tuples().Point(0,0,-3),Tuples().Vector(0,-sqrt(2)/2,sqrt(2)/2))
    i = Intersection(sqrt(2),shape)
    comps = Computations().prepare_computations(i,r)
    color = w.reflected_color(comps)
    assert color == Colors(0.19033,0.23791, 0.14274)
    
    
def test_shade_hit_reflective_material():
    w = World().default_world()
    shape = Planes()
    shape.material.reflective = 0.5
    shape.transform = Transformations.translation(0,-1,0)
    w.objects.append(shape)
    r = Rays(Tuples().Point(0,0,-3),Tuples().Vector(0,-sqrt(2)/2,sqrt(2)/2))
    i = Intersection(sqrt(2),shape)
    comps = Computations().prepare_computations(i,r)
    color = comps.shade_hit(w,comps)
    assert color == Colors(0.87675, 0.92434, 0.82917)
    
def test_mutually_reflective_surfaces():
    w = World()
    w.light.point_light(Tuples().Point(0,0,0),Colors(1,1,1))
    lower = Planes()
    lower.material.reflective = 1
    lower.transform = Transformations.translation(0,-1,0)
    w.objects.append(lower)
    upper = Planes()
    upper.material.reflective = 1
    upper.transform = Transformations.translation(0,1,0)
    w.objects.append(upper)
    r = Rays(Tuples().Point(0,0,0),Tuples().Vector(0,1,0))
    color = Computations().color_at(w,r)
    assert True == True
    
def test_shade_hit_reflective_material_maxrecursion():
    w = World().default_world()
    shape = Planes()
    shape.material.reflective = 0.5
    shape.transform = Transformations.translation(0,-1,0)
    w.objects.append(shape)
    r = Rays(Tuples().Point(0,0,-3),Tuples().Vector(0,-sqrt(2)/2,sqrt(2)/2))
    i = Intersection(sqrt(2),shape)
    comps = Computations().prepare_computations(i,r)
    color = w.reflected_color(comps,0)
    assert color == Colors(0, 0, 0)
    
def test_refracted_color_opaque_surface():
    w = World().default_world()
    shape = w.objects[1]
    r = Rays(Tuples().Point(0,0,-5),Tuples().Vector(0,0,1))
    xs = Intersection.intersections(Intersection(4,shape),Intersection(6,shape))
    comps = Computations().prepare_computations(xs[0],r,xs)
    c = w.refracted_color(comps,5)
    assert c == Colors(0,0,0)
    
def test_refracted_color_maximum_recursion():
    w = World().default_world()
    shape = w.objects[1]
    shape.transparency = 1.0
    shape.refractive_index = 1.5
    r = Rays(Tuples().Point(0,0,-5),Tuples().Vector(0,0,1))
    xs = Intersection.intersections(Intersection(4,shape),Intersection(6,shape))
    comps = Computations().prepare_computations(xs[0],r,xs)
    c = w.refracted_color(comps,0)
    assert c == Colors(0,0,0)
    
    
def test_refracted_color_under_total_internal_reflection():
    w = World().default_world()
    shape = w.objects[1]
    shape.transparency = 1.0
    shape.refractive_index = 1.5
    r = Rays(Tuples().Point(0,0,sqrt(2)/2),Tuples().Vector(0,1,0))
    xs = Intersection.intersections(Intersection(-sqrt(2)/2,shape),Intersection(sqrt(2)/2,shape))
    comps = Computations().prepare_computations(xs[1],r,xs)
    c = w.refracted_color(comps,5)
    assert c == Colors(0,0,0)
    
def test_refracted_color_refracted_ray():
    w = World().default_world()
    a = w.objects[0]
    a.material.ambient = 1.0
    a.material.pattern = Patterns()
    b = w.objects[1]
    b.material.transparency = 1.0
    b.material.refractive_index = 1.5
    r = Rays(Tuples().Point(0,0,0.1),Tuples().Vector(0,1,0))
    xs = Intersection.intersections(Intersection(-0.9899,a),Intersection(-0.4899,b), Intersection(0.4899,b), Intersection(0.9899,a))
    comps = Computations().prepare_computations(xs[2],r,xs)
    c = w.refracted_color(comps,5)
    print(c)
    assert c == Colors(0,0.99888,0.04725)