import pytest

from rayTracer.canvas import Canvas

from rayTracer.colors import Colors


@pytest.fixture
def canvas_10x20():
    return Canvas(10, 20)

@pytest.fixture
def canvas_5x3():
    return Canvas(5, 3)

def test_creating_canvas(canvas_10x20):
    c = canvas_10x20
    assert c.height == 20
    assert c.width == 10

def test_writing_pixels_canvas(canvas_10x20):
    c = canvas_10x20
    red = Colors(1, 0, 0)
    c.write_pixel(2, 3, red)
    assert c.pixel_at(2, 3) == red * 255

def test_construct_ppm(canvas_10x20, tmp_path):
    c = canvas_10x20
    ppm_file = tmp_path / "prueba.ppm"
    c.canvas_to_ppm(ppm_file)
    
    with open(ppm_file, 'r') as file:
        lines = file.readlines()
    
    assert lines[0].strip() == "P3"
    assert lines[1].strip() == "10 20"
    assert lines[2].strip() == "255"
    
def test_construct_ppm2(canvas_5x3, tmp_path):
    c = canvas_5x3
    c1 = Colors(1.5, 0, 0)
    c2 = Colors(0, 0.5, 0)
    c3 = Colors(-0.5, 0, 1)
    
    c.write_pixel(0, 0, c1)
    c.write_pixel(2, 1, c2)
    c.write_pixel(4, 2, c3)
    
    ppm_file = tmp_path / "prueba.ppm"
    c.canvas_to_ppm(ppm_file)
    
    with open(ppm_file, 'r') as file:
        lines = file.readlines()
    
    assert lines[3].strip() == "255 0 0 0 0 0 0 0 0 0 0 0 0 0 0"
    assert lines[4].strip() == "0 0 0 0 0 0 0 128 0 0 0 0 0 0 0"
    assert lines[5].strip() == "0 0 0 0 0 0 0 0 0 0 0 0 0 0 255"
def test_construct_ppm3(tmp_path):
    c1 = Colors(1, 0.8, 0.6)
    c = Canvas(10, 2, c1)
    
    ppm_file = tmp_path / "prueba.ppm"
    c.canvas_to_ppm(ppm_file)
    
    with open(ppm_file, 'r') as file:
        lines = file.readlines()
    
    assert lines[3].strip() == "255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204"
    assert lines[4].strip() == "153 255 204 153 255 204 153 255 204 153 255 204 153"
    assert lines[5].strip() == "255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204"
    
