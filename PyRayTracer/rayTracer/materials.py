from rayTracer.colors import Colors
from rayTracer.patterns import Patterns
from math import pow

EPSILON = 0.00001

class Materials:
    def __init__(self) -> None:
        color = Colors(1, 1, 1)
        self.color = color
        self.ambient = 0.1
        self.diffuse = 0.9
        self.specular = 0.9
        self.shininess = 200.0
        self.pattern = Patterns()
        self.reflective = 0.0
        self.transparecy = 0.0
        self.refractive_index = 1.0
        
        
    def __eq__(self, __value: object) -> bool:
            if (self.color == __value.color and self.equal(self.ambient,__value.ambient) and self.equal(self.diffuse,__value.diffuse) and self.equal(self.specular,__value.specular) and self.equal(self.shininess,__value.shininess)):
                return True
            else:
                 return False

    def equal(self,n1,n2):
        if (abs(n1-n2) < EPSILON):
            return True
        else:
            return False 

    def __str__(self) -> str:
        return "color: " + str(self.color) + " ambient: " + str(self.ambient)  + " diffuse: " + str(self.diffuse)  + " specular: " + str(self.specular)  + " shininess: " + str(self.shininess)
    