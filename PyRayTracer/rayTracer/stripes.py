from rayTracer.colors import Colors
from rayTracer.matrix import Matrix
from rayTracer.patterns import Patterns
from math import floor
class Stripes(Patterns):
    def __init__(self) -> None:
        super().__init__()
                
    def local_pattern(self,a,b):
        self.declared = True
        self.a = a
        self.b = b
        return self
        
    def local_pattern_at(self,point):
        if(floor(point.x) % 2 == 0):
            return self.a
        else:
            return self.b
        
    