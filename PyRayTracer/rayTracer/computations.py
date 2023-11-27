from rayTracer.lights import Lights
from math import sqrt

EPSILON = 0.00001


class Computations:
    def __init__(self) -> None:
        pass
    
    
    def prepare_computations(self,intersection,ray,xs = None):
                
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
        self.under_point = self.point - self.normalv * EPSILON
        
        containers = []
        if xs is not None:
            for i in xs:
                if i == intersection:
                    if not containers:
                        self.n1 = 1.0
                    else:
                        self.n1 = containers[-1].material.refractive_index
                if i.obj in containers:
                    containers.remove(i.obj)
                else:
                    containers.append(i.obj)
                if i == intersection:
                    if not containers:
                        self.n2 = 1.0
                    else:
                        self.n2 = containers[-1].material.refractive_index
                    break
        
        return self
    
    def shade_hit(self,world,remaining = 5):
        shadowed = world.is_shadowed(self.over_point)
        
        surface = Lights().lighting(self.object.material,
                                    self.object,
                                    world.light,
                                    self.over_point, self.eyev, self.normalv,
                                    shadowed)
        
        reflected = world.reflected_color(self,remaining)
        
        refracted = world.refracted_color(self,remaining)
        
        material = self.object.material
        
        if material.reflective > 0 and material.transparency > 0:
            reflectance = self.schlick()
            
            return surface + reflected * reflectance + refracted * (1 - reflectance)
        else:
            return surface + reflected + refracted

    

            
    def schlick(self):
        cos  = self.eyev.dot(self.normalv)
        if self.n1 > self.n2:
            n = self.n1 / self.n2
            sin2_t = n**2 * (1.0 - cos**2)
            if sin2_t > 1.0:
                return 1.0
            cos_t = sqrt(1.0 - sin2_t)
            
            cos = cos_t
        r0 = ((self.n1 - self.n2)/(self.n1 + self.n2))**2
        
        return round((r0 + (1 - r0) * (1 - cos)**5),5)
