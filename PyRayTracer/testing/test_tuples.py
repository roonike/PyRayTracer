from math import sqrt
import pytest

from rayTracer.tuples import Tuples


def test_tuples_1(): 
    t1 = Tuples().Point(4.3, -4.2, 3.1)
    t2 = Tuples().Vector(4.3, -4.2, 3.1)
    print(t1)
    print(True == t1.isPoint())
    print(True == t2.isVector())
    assert True == t1.isPoint()
    assert True == t2.isVector()
    
def test_tuples_2(): 
    t1 = Tuples().Point(4.3, -4.2, 3.1)
    t2 = Tuples().Vector(4.3, -4.2, 3.1)
    assert False == t1.isVector()
    assert False == t2.isPoint()

def test_tuples_add(): 
    t1 = Tuples().Point(3, -2, 5)
    t2 = Tuples().Vector(-2, 3, 1)
    expected = Tuples().Point(1,1,6)
    assert True == ( expected == (t1 + t2) )

def test_tuples_subtract(): 
    t1 = Tuples().Point(3, 2, 1)
    t2 = Tuples().Point(5, 6, 7)
    expected = Tuples().Vector(-2, -4, -6)
    assert True == ( expected == (t1 - t2))

def test_tuples_subtract_vector_point():
    t1 = Tuples().Point(3, 2, 1)
    t2 = Tuples().Vector(5, 6, 7)
    expected = Tuples().Point(-2, -4, -6)
    assert True == ( expected == (t1 - t2))
    
def test_tuples_subtract_vectors():
    t1 = Tuples().Vector(3, 2, 1)
    t2 = Tuples().Vector(5, 6, 7)
    expected = Tuples().Vector(-2, -4, -6)
    assert True == ( expected == (t1 - t2))
    
def test_tuples_negating_tuples():
    t1 = Tuples(1, -2, 3, -4)
    expected = Tuples(-1, 2, -3, 4)
    assert True == ( expected == -t1)
    
def test_tuples_multiplying_tuples_scalar():
    t1 = Tuples(1, -2, 3, -4)
    expected = Tuples(3.5, -7, 10.5, -14)
    assert True == ( expected == t1 * 3.5)
    
def test_tuples_multiplying_tuples_scalar_2():
    t1 = Tuples(1, -2, 3, -4)
    expected = Tuples(0.5, -1, 1.5, -2)
    assert True == ( expected == t1 * 0.5)
    
def test_tuples_dividing():
    t1 = Tuples(1, -2, 3, -4)
    expected = Tuples(0.5, -1, 1.5, -2)
    assert True == ( expected == t1 / 2)

def test_tuples_compute_magnitude():
    t1 = Tuples(1,0,0,0)
    assert True == ( t1.equal(t1.magnitude(),1))
 
def test_tuples_compute_magnitude2():
    t1 = Tuples(0,1,0,0)
    assert True == ( t1.equal(t1.magnitude(),1))   
    
def test_tuples_compute_magnitude3():
    t1 = Tuples(0,0,1,0)
    assert True == ( t1.equal(t1.magnitude(),1))  
    
def test_tuples_compute_magnitude4():
    t1 = Tuples(1,2,3,0)
    assert True == ( t1.equal(t1.magnitude(),sqrt(14)))   
    
def test_tuples_compute_magnitude5():
    t1 = Tuples(-1,-2,-3,0)
    assert True == ( t1.equal(t1.magnitude(),sqrt(14)))   
    
def test_tuples_normalizing_vector():
    t1 = Tuples().Vector(4,0,0)
    expected = Tuples().Vector(1,0,0)
    assert True == (expected == t1.normalize())
    
'''

def test_tuples_normalizing_vector2():
    t1 = Tuples().Vector(1,2,3)
    expected = Tuples().Vector(1/sqrt(14),2/sqrt(14),3/sqrt(14))
    assert True == (expected == t1.normalize())  
    
def test_tuples_normalizing_vector3():
    t1 = Tuples().Vector(1,2,3)
    normalized = t1.normalize()
    assert True == (normalized.equal(1, normalized.magnitude()))  
    
def test_tuples_dot_product_vectors():
    t1 = Tuples().Vector(1,2,3)
    t2 = Tuples().Vector(2,3,4)
    assert True == (t1.dot(t1,t2) == 20)
    
def test_tuples_cross_product_vectors():
    t1 = Tuples().Vector(1,2,3)
    t2 = Tuples().Vector(2,3,4)
    expected1 = Tuples().Vector(-1,2,-1)
    expected2 = Tuples().Vector(1,-2,1)
    assert True == (t1.cross(t1,t2) == expected1)
    assert True == (t1.cross(t2,t1) == expected2)
    
def test_tuples_reflecting_vector_45():
    t1 = Tuples().Vector(1, -1, 0)
    t2 = Tuples().Vector(0, 1, 0)
    expected = Tuples().Vector(1, 1, 0)
    assert True == (t1.reflect(t1, t2) == expected) 

def test_tuples_reflecting_vector_slanted_surface():
    t1 = Tuples().Vector(0, -1, 0)
    t2 = Tuples().Vector(sqrt(2)/2, sqrt(2)/2, 0)
    expected = Tuples().Vector(1, 0, 0)
    assert True == (t1.reflect(t1, t2) == expected) 
    
    '''