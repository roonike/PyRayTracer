from rayTracer.sphere import Sphere
from rayTracer.tuples import Tuples
from rayTracer.rays import Rays
from math import sqrt

class Intersection:
    def __init__(self,t = 0,obj = Sphere()) -> None:
        self.obj = obj
        self.t = t
    
    def intersect(ray):
        sphereToRay = ray.origin - Tuples().Point(0,0,0)
        a = ray.direction.dot(ray.directipon)
        b = 2 * ray.direction.dot(sphereToRay)
        c = sphereToRay.dot(sphereToRay) - 1
        discriminant = pow(b,2) - 4 * a * c
        if discriminant >= 0:
            t1 = (-b - sqrt(discriminant)) / (2*a)
            t2 = (-b + sqrt(discriminant)) / (2*a)
            return (t1,t2)
        else:
            return 0


    def intersections(*iS):
        interesections = []
        for i in iS:
            interesections.append(i)
        return interesections
    
    def hit(self,xs):
        return xs[0]
    
    
    def transform(self,ray,trans):
        return Rays(trans*ray.origin,trans*ray.direction)
    
