from rayTracer.tuples import Tuples

class Rays:
    def __init__(self,origin = Tuples().Point(0,0,0), direction = Tuples().Vector(0,0,0)) -> None:
        self.origin = origin
        self.direction  = direction

    def position (self,t):
        return self.origin + self.direction * t