from rayTracer.tuples import Tuples
from rayTracer.shapes import Shapes
from rayTracer.intersection import Intersection
from math import sqrt

class Sphere(Shapes):
    def __init__(self) -> None:
        super().__init__()
    
    def local_intersect(self,ray):   
        xs = []
        sphereToRay = ray.origin - Tuples().Point(0,0,0)
        a = ray.direction.dot(ray.direction)
        b = 2 * ray.direction.dot(sphereToRay)
        c = sphereToRay.dot(sphereToRay) - 1
        discriminant = (b ** 2) - 4 * a * c
        if discriminant >= 0:
            t1 = Intersection((-b - sqrt(discriminant)) / (2 * a),self)
            t2 = Intersection((-b + sqrt(discriminant)) / (2 * a),self)
            xs.append(t1)
            xs.append(t2)
        return xs

    def local_normal_at(self,point):
        return Tuples().Vector(point.x,point.y,point.z)
    
