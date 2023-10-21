from rayTracer.materials import Materials
from rayTracer.transformations import Transformations
from rayTracer.tuples import Tuples
from rayTracer.rays import Rays
import uuid

class Sphere:
    def __init__(self) -> None:
        self.id = uuid.uuid1()
        self.material = Materials()
        self.transform = Transformations()

    def set_transform(self,transform):
        self.transform = transform

    def normal_at(self,point):
        objectPoint = self.transform.matrix.inverse() * point
        objectNormal = objectPoint - Tuples().Point(0,0,0)
        worldNormal = self.transform.matrix.inverse().transposing() * objectNormal
        worldNormal.w = 0
        return worldNormal.normalize()

