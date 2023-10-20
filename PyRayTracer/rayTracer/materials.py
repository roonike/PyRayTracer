from rayTracer.colors import Colors
from math import pow

class Materials:
    def __init__(self) -> None:
        color = Colors(1, 1, 1)
        self.color = color
        self.ambient = 0.1
        self.diffuse = 0.9
        self.specular = 0.9
        self.shininess = 200.0
        
    