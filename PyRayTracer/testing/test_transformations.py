import math
import pytest
from rayTracer.transformations import Transformations 
from rayTracer.matrix import Matrix
from rayTracer.tuples import Tuples

@pytest.fixture
def sample_point():
    tuple = Tuples()
    return tuple.Point(1, 0, 1)

def test_multiplying_translation():
    t = Transformations().translation(5, -3, 2)
    p = Tuples().Point(-3, 4, 5)
    expected = Tuples().Point(2, 1, 7)
    assert t * p == expected
    

def test_multiplying_translation_inverse():
    p = Tuples().Point(-3, 4, 5)
    expected = Tuples().Point(-8, 7, 3)
    a = Transformations().translation(5, -3, 2)
    inverse = a.inverse()
    result = inverse * p
    assert result == expected

def test_multiplying_translation_vector():
    p = Tuples().Vector(-3, 4, 5)
    a = Transformations().translation(5, -3, 2)
    result = a * p
    assert result == p


def test_scaling_matrix_point():
    p = Tuples().Point(-4, 6, 8)
    expected = Tuples().Point(-8, 18, 32)
    transform = Transformations().scaling(2, 3, 4)
    result = transform * p
    assert result == expected

def test_scaling_matrix_vector():
    v = Tuples().Vector(-4, 6, 8)
    expected = Tuples().Vector(-8, 18, 32)
    transform = Transformations().scaling(2, 3, 4)
    result = transform * v
    assert result == expected

def test_scaling_inverse_vector():
    v = Tuples().Vector(-4, 6, 8)
    expected = Tuples().Vector(-2, 2, 2)
    transform = Transformations().scaling(2, 3, 4)
    inverse = transform.inverse()
    result = inverse * v
    assert result == expected

def test_reflection_scaling():
    p = Tuples().Point(2, 3, 4)
    expected = Tuples().Point(-2, 3, 4)
    transform = Transformations().scaling(-1, 1, 1)
    result = transform * p
    assert result == expected

def test_rotating_point_x():
    p = Tuples().Point(0, 1, 0)
    expected1 = Tuples().Point(0, math.sqrt(2) / 2, math.sqrt(2) / 2)
    expected2 = Tuples().Point(0, 0, 1)
    halfQuarter = Transformations().rotation_x(math.pi / 4)
    fullQuarter = Transformations().rotation_x(math.pi / 2)
    result1 = halfQuarter * p
    result2 = fullQuarter * p
    assert result1 == expected1
    assert result2 == expected2

def test_rotating_inverse_point_x():
    p = Tuples().Point(0, 1, 0)
    expected1 = Tuples().Point(0, math.sqrt(2) / 2, -math.sqrt(2) / 2)
    halfQuarter = Transformations().rotation_x(math.pi / 4)
    inv = halfQuarter.inverse()
    result = inv * p
    assert result == expected1

def test_rotating_point_y():
    p = Tuples().Point(0, 0, 1)
    expected1 = Tuples().Point(math.sqrt(2) / 2, 0, math.sqrt(2) / 2)
    expected2 = Tuples().Point(1, 0, 0)
    halfQuarter = Transformations().rotation_y(math.pi / 4)
    fullQuarter = Transformations().rotation_y(math.pi / 2)
    result1 = halfQuarter * p
    result2 = fullQuarter * p
    assert result1 == expected1
    assert result2 == expected2

def test_rotating_point_z():
    p = Tuples().Point(0, 1, 0)
    expected1 = Tuples().Point(-math.sqrt(2) / 2, math.sqrt(2) / 2, 0)
    expected2 = Tuples().Point(-1, 0, 0)
    halfQuarter = Transformations().rotation_z(math.pi / 4)
    fullQuarter = Transformations().rotation_z(math.pi / 2)
    result1 = halfQuarter * p
    result2 = fullQuarter * p
    assert result1 == expected1
    assert result2 == expected2

def test_shearing_x_in_y():
    p = Tuples().Point(2, 3, 4)
    expected = Tuples().Point(5, 3, 4)
    transform = Transformations().shearing(1, 0, 0, 0, 0, 0)
    result = transform * p
    assert result == expected

def test_shearing_x_in_z():
    p = Tuples().Point(2, 3, 4)
    expected = Tuples().Point(6, 3, 4)
    transform = Transformations().shearing(0, 1, 0, 0, 0, 0)
    result = transform * p
    assert result == expected

def test_shearing_y_in_x():
    p = Tuples().Point(2, 3, 4)
    expected = Tuples().Point(2, 5, 4)
    transform = Transformations().shearing(0, 0, 1, 0, 0, 0)
    result = transform * p
    assert result == expected

def test_shearing_y_in_z():
    p = Tuples().Point(2, 3, 4)
    expected = Tuples().Point(2, 7, 4)
    transform = Transformations().shearing(0, 0, 0, 1, 0, 0)
    result = transform * p
    assert result == expected

def test_shearing_z_in_x():
    p = Tuples().Point(2, 3, 4)
    expected = Tuples().Point(2, 3, 6)
    transform = Transformations().shearing(0, 0, 0, 0, 1, 0)
    result = transform * p
    assert result == expected

def test_shearing_z_in_y():
    p = Tuples().Point(2, 3, 4)
    expected = Tuples().Point(2, 3, 7)
    transform = Transformations().shearing(0, 0, 0, 0, 0, 1)
    result = transform * p
    assert result == expected

def test_individual_transformations(sample_point):
    p = sample_point
    expected1 = Tuples().Point(1, -1, 0)
    expected2 = Tuples().Point(5, -5, 0)
    expected3 = Tuples().Point(15, 0, 7)
    A = Transformations().rotation_x(math.pi / 2)
    B = Transformations().scaling(5, 5, 5)
    C = Transformations().translation(10, 5, 7)
    p2 = A * p
    assert p2 == expected1
    p3 = B * p2
    assert p3 == expected2
    p4 = C * p3
    assert p4 == expected3

def test_chained_transformations(sample_point):
    p = sample_point
    expected1 = Tuples().Point(15, 0, 7)
    A = Transformations().rotation_x(math.pi / 2)
    B = Transformations().scaling(5, 5, 5)
    C = Transformations().translation(10, 5, 7)
    T = C * B * A
    result = T * p
    assert result == expected1
    
def test_transformation_matrix_default_orientation():
    p_from = Tuples().Point(0,0,0)
    p_to = Tuples().Point(0,0,-1)
    p_up = Tuples().Vector(0,1,0)
    transformation_matrix = Transformations().view_transform(p_from, p_to, p_up)
    assert transformation_matrix == transformation_matrix.identity()

def test_view_transformation_positive_z():
    p_from = Tuples().Point(0,0,0)
    p_to = Tuples().Point(0,0,1)
    p_up = Tuples().Vector(0,1,0)
    transformation_matrix = Transformations().view_transform(p_from, p_to, p_up)
    assert transformation_matrix == Transformations().scaling(-1, 1, -1)
    
def test_view_transformation_moves_world():
    p_from = Tuples().Point(0,0,8)
    p_to = Tuples().Point(0,0,0)
    p_up = Tuples().Vector(0,1,0)
    transformation_matrix = Transformations().view_transform(p_from, p_to, p_up)
    assert transformation_matrix == Transformations().translation(0, 0, -8)

def test_arbitrary_view_transformation():
    p_from = Tuples().Point(1, 3, 2)
    p_to = Tuples().Point(4, -2, 8)
    p_up = Tuples().Vector(1, 1, 0)
    transformation_matrix = Transformations().view_transform(p_from, p_to, p_up)
    
    expected = Matrix(4, 4)
    
    expected.mat[0][0] = -0.50709
    expected.mat[0][1] = 0.50709
    expected.mat[0][2] = 0.67612
    expected.mat[0][3] = -2.36643
    
    expected.mat[1][0] = 0.76772
    expected.mat[1][1] = 0.60609
    expected.mat[1][2] = 0.12122
    expected.mat[1][3] = -2.82843
    
    expected.mat[2][0] = -0.35857
    expected.mat[2][1] = 0.59761
    expected.mat[2][2] = -0.71714
    expected.mat[2][3] = 0.00000
    
    expected.mat[3][0] = 0.00000
    expected.mat[3][1] = 0.00000
    expected.mat[3][2] = 0.00000
    expected.mat[3][3] = 1.00000
    
    assert transformation_matrix == expected
    