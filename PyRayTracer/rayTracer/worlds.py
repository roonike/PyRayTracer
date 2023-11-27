from rayTracer.sphere import Sphere
from rayTracer.lights import Lights
from rayTracer.colors import Colors
from rayTracer.transformations import Transformations
from rayTracer.tuples import Tuples
from rayTracer.materials import Materials
from rayTracer.rays import Rays
from rayTracer.intersection import Intersection
from math import sqrt
from rayTracer.computations import Computations

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
        
    def intersect_world(self,ray):
        xs = []
        for object in self.objects:
            new = object.intersect(ray)
            xs = xs + new
        xs = [obj for obj in xs if obj.t >= 0.0]
        xs = sorted(xs, key=lambda x: x.t)
        return xs
        
        
    def is_shadowed(self,p):
        v = self.light.position - p
        distance = v.magnitude()
        direction = v.normalize()
        r = Rays(p,direction)
        intersections = self.intersect_world(r)
        h = Intersection().hit(intersections)
        if h != None and h.t < distance:
            return True
        else:
            return False

    def reflected_color(self,comps,remaining = 5):
        if(remaining == 0):
            return Colors(0,0,0)
        reflectivity = comps.object.material.reflective
        if(reflectivity == 0.0):
            return Colors(0,0,0)
        else:
            reflect_ray = Rays(comps.over_point,comps.reflectv)
            color = self.color_at(reflect_ray,remaining-1)
            return color * reflectivity
        
    def refracted_color(self,comps,remaining = 5):
        if comps.object.material.transparency == 0.0:
            return Colors(0,0,0)
        if remaining == 0:
            return Colors(0,0,0)
        
        n_ratio = comps.n1/comps.n2
        cos_i = comps.normalv.dot(comps.eyev)
        sin2_t = n_ratio**2 * (1 - cos_i**2)
        
        if sin2_t > 1:
            return Colors(0,0,0)
        
        cos_t = sqrt(1.0 - sin2_t)
        
        direction = comps.normalv * (n_ratio * cos_i - cos_t) - comps.eyev * n_ratio
        refracted_ray = Rays(comps.under_point , direction)
        transparency = comps.object.material.transparency
        color = self.color_at(refracted_ray, remaining - 1) * transparency
        return color
    
    
    
    def color_at(self,ray,remaining = 5):
        xs = self.intersect_world(ray)
        if not xs:
            return Colors(0,0,0) 
        
        else: 
            comp = Computations().prepare_computations(xs[0],ray,xs)
            return comp.shade_hit(self,remaining)