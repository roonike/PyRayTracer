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
                            Colors(1, 0.9, 1))
    
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
    
    
    red = Sphere()
    red.material = Materials()
    red.material.color = Colors(1,0,0)
    red.transform = Transformations().translation(1,1,0) * Transformations().scaling(0.1,0.1,0.1)
    orange = Sphere()
    orange.material = Materials()
    orange.material.color = Colors(1,0.5,0)
    orange.transform = Transformations().translation(1,1.25,0) * Transformations().scaling(0.2,0.2,0.2)
    yellow = Sphere()
    yellow.material = Materials()
    yellow.material.color = Colors(1,1,0)
    yellow.transform = Transformations().translation(1,1.5,0) * Transformations().scaling(0.3,0.3,0.3)
    green = Sphere()
    green.material = Materials()
    green.material.color = Colors(0,1,0)
    green.transform = Transformations().translation(1,1.75,0) * Transformations().scaling(0.4,0.4,0.4)
    blue = Sphere()
    blue.material = Materials()
    blue.material.color = Colors (0,0,1)
    blue.transform = Transformations().translation(1,2,0) * Transformations().scaling(0.5,0.5,0.5)
    indigo = Sphere()
    indigo.material = Materials()
    indigo.material.color = Colors(0.29,0,0.5)
    indigo.transform = Transformations().translation(1,2.25,0) * Transformations().scaling(0.6,0.6,0.6)
    violet = Sphere()
    violet.material = Materials()
    violet.material.color = Colors(0.58,0,0.82)
    violet.transform = Transformations().translation(1,2.5,0) * Transformations().scaling(0.8,0.8,0.8)
    
    '''
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
    
    '''
    world.objects.append(floor)
    world.objects.append(left_wall) 
    world.objects.append(right_wall)
    world.objects.append(red)
    world.objects.append(orange)
    world.objects.append(yellow)
    world.objects.append(green)
    world.objects.append(blue)
    world.objects.append(indigo)
    world.objects.append(violet)

    camera = Camera(300, 150, math.pi/3)
    camera.transform = Transformations().view_transform(Tuples().Point(0, 1.5, -5),
                                                        Tuples().Point(0, 1, 0),
                                                        Tuples().Vector(0, 1, 0))
    canvas = camera.render(world)
    canvas.canvas_to_ppm("SceneAttmempt.ppm")
    
   
if __name__ == "__main__":
    main()