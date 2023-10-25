from rayTracer.rays import Rays
from rayTracer.intersection import Intersection
from rayTracer.sphere import Sphere
from rayTracer.worlds import World
from rayTracer.lights import Lights

EPSILON = 0.00001

class Computations:
    def __init__(self) -> None:
        pass
    
    def prepare_computations(self,intersection,ray):
        self.t = intersection.t
        self.object = intersection.obj
        self.point = ray.position(self.t)
        self.eyev = -ray.direction
        self.normalv = intersection.obj.normal_at(self.point)
        if self.normalv.dot(self.eyev) < 0:
            self.inside = True
            self.normalv = -self.normalv
        else:
            self.inside = False
        self.over_point = self.point + self.normalv * EPSILON
        return self
    
    def shade_hit(self,world,comps):
        return Lights().lighting(comps.object.material,world.light,comps.point,comps.eyev,comps.normalv)

'''       
    def intersect_worlds(self,world,ray):
            

    def is_shadowed(world,point):
        v = world.light.position - point
        distance = v.magnitude()
        direction = v.normalize()
        
        r = Rays(distance,direction)
        Intersection = intersect_world(world,r)
        pass
'''