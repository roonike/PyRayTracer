from rayTracer.colors import Colors
from rayTracer.tuples import Tuples
from rayTracer.worlds import World
from rayTracer.sphere import Sphere
from rayTracer.planes import Planes
from rayTracer.materials import Materials
from rayTracer.transformations import Transformations
from rayTracer.camera import Camera
from rayTracer.patterns import Patterns
from rayTracer.rings import Rings
from rayTracer.gradient import Gradient
from rayTracer.checkers import Checkers
from rayTracer.stripes import Stripes
import math

def main():
    
    world = World()
    
    world.light.point_light(Tuples().Point(10, 10, -10),
                            Colors(1, 1, 1))
    
    stripes = Stripes().pattern(Colors(1,0,0),Colors(1,0,1))
    rings = Rings().pattern(Colors(1,1,1),Colors(1,0,1))
    gradient = Gradient().pattern(Colors(0,0,0),Colors(1,1,1))
    gradient.set_pattern_transform(Transformations.translation(.5,.2,2))
    checkers = Checkers().pattern(Colors(0,0,0),Colors(1,0,0))
    checkers.set_pattern_transform(Transformations.translation(0.5,1,1.5) * Transformations.scaling(0.25,0.25,0.25))
    
    
    floor = Planes()
    floor.material.pattern = stripes
    wall = Planes()
    wall.set_transform(Transformations().translation(0,0,30)*Transformations().rotation_x(math.pi/2))
    wall.material.pattern = rings
    
    middle = Sphere()
    middle.transform = Transformations().translation(-0.5, 1, 0.5)
    middle.material = Materials()
    middle.material.pattern = checkers
    middle.material.diffuse = 0.7
    middle.material.specular = 0.3
    
    right = Sphere()
    right.transform = Transformations().translation(1.5, 0.5, -0.5) * Transformations().scaling(0.5, 0.5, 0.5)
    right.material = Materials()
    right.material.pattern = gradient
    right.material.diffuse = 0.7
    right.material.specular = 0.3
    
    left = Sphere()
    left.transform = Transformations().translation(-1.5, 0.33, -0.75) * Transformations().scaling(0.33, 0.33, 0.33)
    left.material = Materials()
    left.material.pattern = stripes
    left.material.diffuse = 0.7
    left.material.specular = 0.3
    
    
    
    world.objects.append(middle)
    world.objects.append(right)
    world.objects.append(left)
    world.objects.append(floor)
    world.objects.append(wall)
    
    camera = Camera(200, 150, math.pi/3)
    camera.transform = Transformations().view_transform(Tuples().Point(2, 1, -5),
                                                        Tuples().Point(0, 0, 0),
                                                        Tuples().Vector(0, 1, 0))
    canvas = camera.render(world)
    canvas.canvas_to_ppm("planetest.ppm")
    
   
if __name__ == "__main__":
    
    main()