from rayTracer.matrix import Matrix
from rayTracer.materials import Materials
from rayTracer.tuples import Tuples
from rayTracer.rays import Rays
import uuid

class Shapes:
    def __init__(self) -> None:
        self.material = Materials()
        self.transform = Matrix(4,4).identity()
        self.saved_ray = Rays()
        self.id = uuid.uuid1()
        pass
    
    def __eq__(self, __value: object) -> bool:
        return self.material == __value.material and self.transform == __value.transform
    
    def set_transform(self,transform):
        self.transform = transform
        return self

    def normal_at(self,point):
        local_point = self.transform.inverse() * point
        local_normal = self.local_normal_at(local_point)
        world_normal = self.transform.inverse().transposing() * local_normal
        world_normal.w = 0
        return world_normal.normalize()
    
    def intersect(self,ray):
        local_ray = self.ray_transform(ray , self.transform.inverse())
        return self.local_intersect(local_ray)
    
    def ray_transform(self,ray,trans):
        return Rays(trans*ray.origin,trans*ray.direction)
    
    def local_normal_at(self,point):
        return Tuples().Vector(point.x,point.y,point.z)
    
    def local_intersect(self,ray):
        self.saved_ray = ray
        
    def glass(self):
        self.material.transparecy = 1.0
        self.material.refractive_index = 1.5
        return self