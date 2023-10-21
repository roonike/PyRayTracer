from rayTracer.colors import Colors
from rayTracer.tuples import Tuples
from rayTracer.worlds import World
from rayTracer.sphere import Sphere
from rayTracer.materials import Materials
from rayTracer.transformations import Transformations
from rayTracer.camera import Camera
import math

def main():
    
    world = World()
    
    world.light.point_light(Tuples().Point(-10, 10, -10),
                            Colors(1, 1, 1))
    
    floor = Sphere()
    floor.transform = Transformations().scaling(10, 0.01, 10)
    floor.material = Materials()
    floor.material.color = Colors(1, 0.9, 0.9)
    floor.material.specular = 0
    
    left_wall = Sphere()
    left_wall.transform = Transformations().translation(0, 0, 5) * Transformations().rotation_y(-math.pi/4) * Transformations().rotation_x(math.pi/2) * Transformations().scaling(10, 0.01, 10)
    left_wall.material = floor.material
    
    right_wall = Sphere()
    right_wall.transform = Transformations().translation(0, 0, 5) * Transformations().rotation_y(math.pi/4) * Transformations().rotation_x(math.pi/2) * Transformations().scaling(10, 0.01, 10)
    right_wall.material = floor.material
    
    middle = Sphere()
    middle.transform = Transformations().translation(-0.5, 1, 0.5)
    middle.material = Materials()
    middle.material.color = Colors(0.1, 1, 0.5)
    middle.material.diffuse = 0.7
    middle.material.specular = 0.3
    
    right = Sphere()
    right.transform = Transformations().translation(1.5, 0.5, -0.5) * Transformations().scaling(0.5, 0.5, 0.5)
    right.material = Materials()
    right.material.color = Colors(0.5, 1, 0.1)
    right.material.diffuse = 0.7
    right.material.specular = 0.3
    
    left = Sphere()
    left.transform = Transformations().translation(-1.5, 0.33, -0.75) * Transformations().scaling(0.33, 0.33, 0.33)
    left.material = Materials()
    left.material.color = Colors(1, 0.8, 0.1)
    left.material.diffuse = 0.7
    left.material.specular = 0.3
    
    
    world.objects.append(floor)
    world.objects.append(left_wall) 
    world.objects.append(right_wall)
    world.objects.append(middle)
    world.objects.append(right)
    world.objects.append(left)

    camera = Camera(300, 150, math.pi/3)
    camera.transform = Transformations().view_transform(Tuples().Point(0, 1.5, -5),
                                                        Tuples().Point(0, 1, 0),
                                                        Tuples().Vector(0, 1, 0))
    canvas = camera.render(world)
    canvas.canvas_to_ppm("purpleCircle2.ppm")
    
   
if __name__ == "__main__":
    main()