import pytest
from rayTracer.worlds import Worlds
from rayTracer.rays import Rays
from rayTracer.sphere import Sphere
from rayTracer.intersection import Intersection
from rayTracer.computations import Computations
from rayTracer.tuples import Tuples
from rayTracer.colors import Colors
from rayTracer.lights import Lights
from rayTracer.materials import Materials
from rayTracer.transformations import Transformations

def test_creating_world():
    world = Worlds()
    assert len(world.objects) == 0

def test_creating_default_world():
    world = Worlds()
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

    assert world.light == light
    assert s1 in world.objects
    assert s2 in world.objects

def test_intersect_world_ray():
    world = Worlds()
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
    world = Worlds()
    world.default_world()

    origin = Tuples().Point(0, 0, -5)
    direction = Tuples().Vector(0, 0, 1)
    ray = Rays(origin, direction)

    shape = world.objects[0]

    i = Intersection(4, shape)
    com = Computations()
    comps = com.prepare_computations(i, ray)
    c = com.shade_hit(world, comps)
    col = Colors(0.38066, 0.47583, 0.2855)
    print(str(c))
    print(str(col))
    assert c == col

def test_shading_intersection_inside():
    world = Worlds()
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
    c = com.shade_hit(world, comps)
    col = Colors(0.90498, 0.90498, 0.90498)

    assert c == col

def test_color_ray_misses():
    world = Worlds()
    world.default_world()

    origin = Tuples().Point(0, 0, -5)
    direction = Tuples().Vector(0, 1, 0)
    ray = Rays(origin, direction)

    com = Computations()
    c = com.color_at(world, ray)
    col = Colors(0, 0, 0)

    assert c == col

def test_color_ray_hits():
    world = Worlds()
    world.default_world()

    origin = Tuples().Point(0, 0, -5)
    direction = Tuples().Vector(0, 0, 1)
    ray = Rays(origin, direction)

    com = Computations()
    c = com.color_at(world, ray)
    col = Colors(0.38066, 0.47583, 0.2855)

    assert c == col

def test_color_intersection_behind_ray():
    world = Worlds()
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

    assert c == inner.material.color