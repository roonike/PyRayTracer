from rayTracer.shapes import Shapes
from rayTracer.tuples import Tuples
from rayTracer.intersection import Intersection
EPSILON = 0.00001

class Planes(Shapes):
    def __init__(self) -> None:
        super().__init__()
        
    def local_normal_at(self, point):
        return Tuples().Vector(0,1,0)
    
    def local_intersect(self, ray):
        xs = []
        if ray.direction.y == 0:
            return xs
        xs.append(Intersection((-(ray.origin.y)/ray.direction.y) , self))
        return xs