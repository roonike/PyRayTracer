import pytest

from rayTracer.colors import Colors

def test_create_color():
	c = Colors(-0.5, 0.4, 1.7)
	assert(c.r == -0.5)
	assert(c.g == 0.4)
	assert(c.b == 1.7)


def test_add_colors():
	c1 = Colors(0.9, 0.6, 0.75)
	c2 = Colors(0.7, 0.1, 0.25)
	expectedC = Colors(1.6, 0.7, 1.0)
	assert(expectedC == c1 + c2)


def test_subtracting_colors():
	c1 = Colors(0.9, 0.6, 0.75)
	c2 = Colors(0.7, 0.1, 0.25)
	expectedC = Colors(0.2, 0.5, 0.5)
	assert(expectedC == c1 - c2)


def test_multiplying_Color_Scalar():
    c1 = Colors(0.2, 0.3, 0.4) 
    expectedC = Colors(0.4, 0.6, 0.8)
    assert(expectedC == c1 * 2)


def test_multiplying_colors():
    c1 = Colors(1, 0.2, 0.4)
    c2 = Colors(0.9, 1, 0.1)
    expectedC = Colors(0.9, 0.2, 0.04)
    assert(expectedC == c1 * c2)
