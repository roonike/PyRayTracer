from rayTracer.materials import Materials
from rayTracer.transformations import Transformations
from rayTracer.matrix import Matrix
from rayTracer.tuples import Tuples
from rayTracer.rays import Rays
import uuid

class Sphere:
    def __init__(self) -> None:
        self.id = uuid.uuid1()
        self.material = Materials()
        self.transform = Matrix(4,4).identity()

    def set_transform(self,transform):
        self.transform = transform
        return self

    def normal_at(self,point):
        objectPoint = self.transform.inverse() * point
        objectNormal = objectPoint - Tuples().Point(0,0,0)
        worldNormal = self.transform.inverse().transposing() * objectNormal
        worldNormal.w = 0
        return worldNormal.normalize()
    
    def __eq__(self, __value: object) -> bool:
        return self.material == __value.material and self.transform == __value.transform
        pass
    

