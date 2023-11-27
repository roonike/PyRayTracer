from rayTracer.tuples import Tuples
from rayTracer.rays import Rays
from rayTracer.shapes import Shapes
from math import sqrt


class Intersection:
    def __init__(self,t = 0, obj = None) -> None:
        self.obj = obj
        self.t = t

    @staticmethod
    def intersections(*iS):
        return list(iS)
    
    def hit(self,xs):
        if len(xs) == 0:
            return None
        lowest = xs[0]
        for i in range(1,len(xs)):
            if xs[i].t < lowest.t and xs[i].t >= 0 or lowest.t < 0:
                lowest = xs[i]
        
        if(lowest.t < 0):
            lowest = None
        return lowest
    
    def intersect_world(self,world,ray):
        xs = []
        for object in world.objects:
          new = object.intersect(ray)
          xs = xs + new
        xs = sorted(xs, key=lambda x: x.t)
        return xs
    
    def transform(self,ray,trans):
        return Rays(trans*ray.origin,trans*ray.direction)
    
    def __str__(self) -> str:
        return "obj = " +  self.obj + " t = " + self.t 