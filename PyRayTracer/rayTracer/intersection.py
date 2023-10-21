from rayTracer.sphere import Sphere
from rayTracer.tuples import Tuples
from rayTracer.rays import Rays
from math import sqrt


class Intersection:
    def __init__(self,t = 0,obj = Sphere()) -> None:
        self.obj = obj
        self.t = t
    
    def intersect(self,sphere,ray):
        xs = []
        ray2 = self.transform(ray, sphere.transform.inverse())
        sphereToRay = ray2.origin - Tuples().Point(0,0,0)
        a = ray2.direction.dot(ray2.direction)
        b = 2 * ray2.direction.dot(sphereToRay)
        c = sphereToRay.dot(sphereToRay) - 1
        discriminant = (b ** 2) - 4 * a * c
        if discriminant >= 0:
            t1 = Intersection((-b - sqrt(discriminant)) / (2 * a),sphere)
            t2 = Intersection((-b + sqrt(discriminant)) / (2 * a),sphere)
            xs.append(t1)
            xs.append(t2)
            return xs
        else:
            return xs


    def intersections(*iS):
        interesections = []
        for i in iS:
            interesections.append(i)
        return interesections
    
    def hit(self,xs):
        return xs[0]
    
    
    def transform(self,ray,trans):
        return Rays(trans*ray.origin,trans*ray.direction)
    
