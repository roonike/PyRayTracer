from rayTracer.colors import Colors
from rayTracer.patterns import Patterns
from rayTracer.sphere import Sphere
from rayTracer.transformations import Transformations   
from rayTracer.tuples import Tuples
from rayTracer.stripes import Stripes
from rayTracer.matrix import Matrix
from rayTracer.gradient import Gradient
from rayTracer.rings import Rings
from rayTracer.checkers import Checkers

black = Colors(0,0,0)
white = Colors(1,1,1)


def test_create_stripe_pattern():
    pattern = Stripes().pattern(white,black)
    assert pattern.a == white
    assert pattern.b == black
    
def test_stripe_pattern_constant_y():
    pattern = Stripes().pattern(white,black)
    assert pattern.pattern_at(Tuples().Point(0,0,0)) == white
    assert pattern.pattern_at(Tuples().Point(0,1,0)) == white
    assert pattern.pattern_at(Tuples().Point(0,2,0)) == white
    
def test_stripe_pattern_constant_z():
    pattern = Stripes().pattern(white,black)
    assert pattern.pattern_at(Tuples().Point(0,0,0)) == white
    assert pattern.pattern_at(Tuples().Point(0,0,1)) == white
    assert pattern.pattern_at(Tuples().Point(0,0,2)) == white
    
def test_stripe_pattern_alternates_x():
    pattern = Stripes().pattern(white,black)
    assert pattern.pattern_at(Tuples().Point(0,0,0)) == white
    assert pattern.pattern_at(Tuples().Point(0.9,0,0)) == white
    assert pattern.pattern_at(Tuples().Point(1,0,0)) == black
    assert pattern.pattern_at(Tuples().Point(-0.1,0,0)) == black
    assert pattern.pattern_at(Tuples().Point(-1,0,0)) == black
    assert pattern.pattern_at(Tuples().Point(-1.1,0,0)) == white
    
def test_stripes_object_transform():
    obj = Sphere()
    obj.set_transform(Transformations.scaling(2,2,2))
    pattern = Stripes().pattern(white,black)
    c = pattern.pattern_at_object(obj,Tuples().Point(1.5,0,0))
    assert c == white
    
def test_stripes_pattern_transform():
    obj = Sphere()
    pattern = Stripes().pattern(white,black)
    pattern = pattern.set_pattern_transform(Transformations.scaling(2,2,2))
    c = pattern.pattern_at_object(obj,Tuples().Point(1.5,0,0))
    print(c)
    print(white)
    assert c == white

def test_stripes_pattern_obj_transform():
    obj = Sphere()
    obj.set_transform(Transformations.scaling(2,2,2))
    pattern = Stripes().pattern(white,black)
    pattern = pattern.set_pattern_transform(Transformations.translation(0.5,0,0))
    c = pattern.pattern_at_object(obj,Tuples().Point(2.5,0,0))
    assert c == white
    
def test_default_pattern():
    pattern = Patterns()
    assert pattern.transform == Matrix(4,4).identity()
    
def test_pattern_assign_transform():
    pattern = Patterns()
    pattern.set_pattern_transform(Transformations().translation(1,2,3))
    assert pattern.transform == Transformations().translation(1,2,3)

def test_generic_pattern_obj_transform():
    obj = Sphere()
    obj.set_transform(Transformations.scaling(2,2,2))
    pattern = Patterns()
    c = pattern.pattern_at_object(obj,Tuples().Point(2,3,4))
    assert c == Colors(1,1.5,2)
    
def test_generic_pattern_transform_obj():
    obj = Sphere()
    pattern = Patterns()
    pattern.set_pattern_transform(Transformations.scaling(2,2,2))
    c = pattern.pattern_at_object(obj,Tuples().Point(2,3,4))
    assert c == Colors(1,1.5,2)
    
    
def test_generic_pattern_obj_pattern_transform():
    obj = Sphere()
    obj.set_transform(Transformations.scaling(2,2,2))
    pattern = Patterns()
    pattern.set_pattern_transform(Transformations.translation(0.5,1,1.5))
    c = pattern.pattern_at_object(obj,Tuples().Point(2.5,3,3.5))
    assert c == Colors(0.75,0.5,0.25)
    
def test_gradient_pattern():
    pattern = Gradient().pattern(white,black)
    assert pattern.pattern_at(Tuples().Point(0,0,0)) == white
    assert pattern.pattern_at(Tuples().Point(0.25,0,0)) == Colors(0.75,0.75,0.75)
    assert pattern.pattern_at(Tuples().Point(0.5,0,0)) == Colors(0.5,0.5,0.5)
    assert pattern.pattern_at(Tuples().Point(0.75,0,0)) == Colors(0.25,0.25,0.25)
    
def test_ring_pattern():
    pattern = Rings().pattern(white,black)
    assert pattern.pattern_at(Tuples().Point(0,0,0)) == white
    assert pattern.pattern_at(Tuples().Point(1,0,0)) == black
    assert pattern.pattern_at(Tuples().Point(0,0,1)) == black
    assert pattern.pattern_at(Tuples().Point(0.708,0,0.708)) == black

def test_3d_checker_pattern_x():
    pattern = Checkers().pattern(white,black)
    assert pattern.pattern_at(Tuples().Point(0,0,0)) == white
    assert pattern.pattern_at(Tuples().Point(0.99,0,0)) == white
    assert pattern.pattern_at(Tuples().Point(1.01,0,0)) == black
    
def test_3d_checker_pattern_y():
    pattern = Checkers().pattern(white,black)
    assert pattern.pattern_at(Tuples().Point(0,0,0)) == white
    assert pattern.pattern_at(Tuples().Point(0,0.99,0)) == white
    assert pattern.pattern_at(Tuples().Point(0,1.01,0)) == black
    
def test_3d_checker_pattern_z():
    pattern = Checkers().pattern(white,black)
    assert pattern.pattern_at(Tuples().Point(0,0,0)) == white
    assert pattern.pattern_at(Tuples().Point(0,0,0.99)) == white
    assert pattern.pattern_at(Tuples().Point(0,0,1.01)) == black
    
    