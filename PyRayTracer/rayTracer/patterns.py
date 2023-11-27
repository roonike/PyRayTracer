from rayTracer.colors import Colors
from rayTracer.matrix import Matrix
from math import floor
class Patterns():
    def __init__(self) -> None:
        self.declared = False
        self.transform = Matrix(4,4).identity()
    
    def test_pattern(self):
        self.declared = True
        return self
    
    def set_pattern_transform(self, transform):
        self.transform = transform
        return self
    
    def pattern_at_object(self, obj, point):
        object_point = obj.transform.inverse() * point
        pattern_point = self.transform.inverse() * object_point
        return self.local_pattern_at(pattern_point)
    
    def pattern(self,a,b):
        return self.local_pattern(a,b)
    
    def local_pattern(self,a,b):
        self.declared = True
        return self.transform
    
    def pattern_at(self,point):
        return self.local_pattern_at(point)        

    def local_pattern_at(self,point):
        return Colors(point.x,point.y,point.z)
        
