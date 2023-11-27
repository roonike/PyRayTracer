from rayTracer.rays import Rays
from rayTracer.intersection import Intersection
from rayTracer.sphere import Sphere
from rayTracer.worlds import World
from rayTracer.lights import Lights
from rayTracer.colors import Colors

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
        self.reflectv = ray.direction.reflect(self.normalv)
        self.over_point = self.point + self.normalv * EPSILON
        return self
    
    def shade_hit(self,world,comps,remaining = 5):
        shadowed = world.is_shadowed(comps.over_point)
        surface = Lights().lighting(comps.object.material,comps.object,world.light,comps.over_point, comps.eyev, comps.normalv,shadowed)
        reflected = world.reflected_color(self,remaining)
        return surface + reflected

    def color_at(self,world,ray,remaining = 5):
        xs = Intersection().intersect_world(world,ray)
        xs = [obj for obj in xs if obj.t >= 0]
        if len(xs) == 0:
            return Colors(0,0,0)
        else:
            comps = self.prepare_computations(xs[0],ray)
            return self.shade_hit(world,comps,remaining)