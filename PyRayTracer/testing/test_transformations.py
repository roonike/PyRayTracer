import math
import pytest
from rayTracer.transformations import Transformations  # Asumiendo que tienes una clase llamada 'Transformations' en un archivo llamado 'transformations.py'
from rayTracer.tuples import Tuple  # Asumiendo que tienes una clase llamada 'Tuple' para representar tuplas

@pytest.fixture
def transformations_instance():
    return Transformations()

@pytest.fixture
def sample_point():
    return Tuple.point(1, 0, 1)

def test_multiplying_translation(transformations_instance):
    p = Tuple.point(-3, 4, 5)
    expected = Tuple.point(2, 1, 7)
    a = transformations_instance.translation(5, -3, 2)
    result = a * p
    assert result == expected

def test_multiplying_translation_inverse(transformations_instance):
    p = Tuple.point(-3, 4, 5)
    expected = Tuple.point(-8, 7, 3)
    a = transformations_instance.translation(5, -3, 2)
    inverse = a.inverse()
    result = inverse * p
    assert result == expected

def test_multiplying_translation_vector(transformations_instance):
    p = Tuple.vector(-3, 4, 5)
    a = transformations_instance.translation(5, -3, 2)
    result = a * p
    assert result == p

def test_scaling_matrix_point(transformations_instance):
    p = Tuple.point(-4, 6, 8)
    expected = Tuple.point(-8, 18, 32)
    transform = transformations_instance.scaling(2, 3, 4)
    result = transform * p
    assert result == expected

def test_scaling_matrix_vector(transformations_instance):
    v = Tuple.vector(-4, 6, 8)
    expected = Tuple.vector(-8, 18, 32)
    transform = transformations_instance.scaling(2, 3, 4)
    result = transform * v
    assert result == expected

def test_scaling_inverse_vector(transformations_instance):
    v = Tuple.vector(-4, 6, 8)
    expected = Tuple.vector(-2, 2, 2)
    transform = transformations_instance.scaling(2, 3, 4)
    inverse = transform.inverse()
    result = inverse * v
    assert result == expected

def test_reflection_scaling(transformations_instance):
    p = Tuple.point(2, 3, 4)
    expected = Tuple.point(-2, 3, 4)
    transform = transformations_instance.scaling(-1, 1, 1)
    result = transform * p
    assert result == expected

def test_rotating_point_x(transformations_instance):
    p = Tuple.point(0, 1, 0)
    expected1 = Tuple.point(0, math.sqrt(2) / 2, math.sqrt(2) / 2)
    expected2 = Tuple.point(0, 0, 1)
    halfQuarter = transformations_instance.rotation_x(math.pi / 4)
    fullQuarter = transformations_instance.rotation_x(math.pi / 2)
    result1 = halfQuarter * p
    result2 = fullQuarter * p
    assert result1 == expected1
    assert result2 == expected2

def test_rotating_inverse_point_x(transformations_instance):
    p = Tuple.point(0, 1, 0)
    expected1 = Tuple.point(0, math.sqrt(2) / 2, -math.sqrt(2) / 2)
    halfQuarter = transformations_instance.rotation_x(math.pi / 4)
    inv = halfQuarter.inverse()
    result = inv * p
    assert result == expected1

def test_rotating_point_y(transformations_instance):
    p = Tuple.point(0, 0, 1)
    expected1 = Tuple.point(math.sqrt(2) / 2, 0, math.sqrt(2) / 2)
    expected2 = Tuple.point(1, 0, 0)
    halfQuarter = transformations_instance.rotation_y(math.pi / 4)
    fullQuarter = transformations_instance.rotation_y(math.pi / 2)
    result1 = halfQuarter * p
    result2 = fullQuarter * p
    assert result1 == expected1
    assert result2 == expected2

def test_rotating_point_z(transformations_instance):
    p = Tuple.point(0, 1, 0)
    expected1 = Tuple.point(-math.sqrt(2) / 2, math.sqrt(2) / 2, 0)
    expected2 = Tuple.point(-1, 0, 0)
    halfQuarter = transformations_instance.rotation_z(math.pi / 4)
    fullQuarter = transformations_instance.rotation_z(math.pi / 2)
    result1 = halfQuarter * p
    result2 = fullQuarter * p
    assert result1 == expected1
    assert result2 == expected2

def test_shearing_x_in_y(transformations_instance):
    p = Tuple.point(2, 3, 4)
    expected = Tuple.point(5, 3, 4)
    transform = transformations_instance.shearing(1, 0, 0, 0, 0, 0)
    result = transform * p
    assert result == expected

def test_shearing_x_in_z(transformations_instance):
    p = Tuple.point(2, 3, 4)
    expected = Tuple.point(6, 3, 4)
    transform = transformations_instance.shearing(0, 1, 0, 0, 0, 0)
    result = transform * p
    assert result == expected

def test_shearing_y_in_x(transformations_instance):
    p = Tuple.point(2, 3, 4)
    expected = Tuple.point(2, 5, 4)
    transform = transformations_instance.shearing(0, 0, 1, 0, 0, 0)
    result = transform * p
    assert result == expected

def test_shearing_y_in_z(transformations_instance):
    p = Tuple.point(2, 3, 4)
    expected = Tuple.point(2, 7, 4)
    transform = transformations_instance.shearing(0, 0, 0, 1, 0, 0)
    result = transform * p
    assert result == expected

def test_shearing_z_in_x(transformations_instance):
    p = Tuple.point(2, 3, 4)
    expected = Tuple.point(2, 3, 6)
    transform = transformations_instance.shearing(0, 0, 0, 0, 1, 0)
    result = transform * p
    assert result == expected

def test_shearing_z_in_y(transformations_instance):
    p = Tuple.point(2, 3, 4)
    expected = Tuple.point(2, 3, 7)
    transform = transformations_instance.shearing(0, 0, 0, 0, 0, 1)
    result = transform * p
    assert result == expected

def test_individual_transformations(transformations_instance, sample_point):
    p = sample_point
    expected1 = Tuple.point(1, -1, 0)
    expected2 = Tuple.point(5, -5, 0)
    expected3 = Tuple.point(15, 0, 7)
    A = transformations_instance.rotation_x(math.pi / 2)
    B = transformations_instance.scaling(5, 5, 5)
    C = transformations_instance.translation(10, 5, 7)
    p2 = A * p
    assert p2 == expected1
    p3 = B * p2
    assert p3 == expected2
    p4 = C * p3
    assert p4 == expected3

def test_chained_transformations(transformations_instance, sample_point):
    p = sample_point
    expected1 = Tuple.point(15, 0, 7)
    A = transformations_instance.rotation_x(math.pi / 2)
    B = transformations_instance.scaling(5, 5, 5)
    C = transformations_instance.translation(10, 5, 7)
    T = C * B * A
    result = T * p
    assert result == expected1