from rayTracer.sphere import Sphere
from rayTracer.lights import Lights
from rayTracer.colors import Colors
from rayTracer.transformations import Transformations
from rayTracer.tuples import Tuples
from rayTracer.materials import Materials
from rayTracer.rays import Rays
from rayTracer.intersection import Intersection

class World:
    def __init__(self) -> None:
        self.objects = []
        self.light = Lights()
    
    def default_world(self):
        light = Lights()
        point = Tuples().Point(-10, 10, -10)
        color = Colors(1, 1, 1)
        light.point_light(point, color)
        
        self.light = light

        material = Materials()
        material_color = Colors(0.8, 1.0, 0.6)
        material.color = material_color
        material.diffuse = 0.7
        material.specular = 0.2

        s1 = Sphere()
        s1.material = material

        trans = Transformations()
        s2 = Sphere()
        s2.set_transform(trans.scaling(0.5, 0.5, 0.5))
        self.objects.append(s1)
        self.objects.append(s2)
        return self
        
    def is_shadowed(self,p):
        v = self.light.position - p
        distance = v.magnitude()
        direction = v.normalize()
        r = Rays(p,direction)
        intersections = Intersection().intersect_world(self,r)
        h = Intersection().hit(intersections)
        if h != None and h.t < distance:
            return True
        else:
            return False

        