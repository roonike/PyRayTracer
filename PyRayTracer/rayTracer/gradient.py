from rayTracer.patterns import Patterns
from math import floor

class Gradient(Patterns):
    def __init__(self) -> None:
        super().__init__()
        
    def local_pattern(self, a, b):
        self.declared = True
        self.a = a
        self.b = b
        return self
    
    def local_pattern_at(self, point):
        distance = self.b - self.a
        fraction = point.x - floor(point.x)
        return self.a + distance * fraction
        