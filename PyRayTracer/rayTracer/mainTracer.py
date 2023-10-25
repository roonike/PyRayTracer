from rayTracer.canvas import Canvas
from rayTracer.rays import Rays
from rayTracer.colors import Colors
from rayTracer.sphere import Sphere
from rayTracer.tuples import Tuples
from rayTracer.intersection import Intersection

ray_origin = Tuples().Point(0,0,-5)
wall_z = 10
wall_size = 7.0
canvas_pixels = 100
pixel_size = wall_size/canvas_pixels
half = wall_size/2

canvas = Canvas(canvas_pixels,canvas_pixels)
color = Colors(1,0,0)
shape = Sphere()
for y in range(canvas.w):
    world_y = half - pixel_size*y
    for x in range(canvas.h):
        world_x = -half + pixel_size*x
        position = Tuples.Point(world_x,world_y,wall_z) - ray_origin
        position.normalize()
        r = Rays(ray_origin,position)
        xs = Intersection().intersect(shape,r)
        
        if(xs.hit() != None):
            canvas.write_pixel(x,y,color)
            
canvas.canvas_to_ppm("Red ball.ppm")