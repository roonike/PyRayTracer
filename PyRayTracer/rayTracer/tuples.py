from math import sqrt
EPSILON = 0.00001

class Tuples:


    def __init__(self,X = 0, Y = 0, Z = 0, W = 0):
        self.x = X
        self.y = Y 
        self.z = Z
        self.w = W

    def Vector(self,num1, num2, num3):
        self.x = num1
        self.y = num2
        self.z = num3
        self.w = 0
        return self
    
    def Point(self,num1,num2,num3):
        self.x = num1
        self.y = num2
        self.z = num3
        self.w = 1
        return self
    
        
    def __add__(self,o):
        suma = Tuples(self.x + o.x, self.y + o.y, self.z + o.z , self.w + o.w)
        return suma

    def __sub__(self,o):
        resta = Tuples(self.x - o.x, self.y - o.y, self.z - o.z , self.w - o.w)
        return resta

    def __mul__(self,o):
        mul = Tuples(self.x * o , self.y * o , self.z * o , self.w * o)
        return mul
    
    def __rmul__(self,o):
        return self.__mul__(o)


    def __truediv__(self,o):
        div = Tuples(self.x / o , self.y / o , self.z / o , self.w / o)
        return div

    def __neg__(self):
        neg = Tuples(-self.x, -self.y, -self.z, -self.w)
        return neg
    
    def equal(self,n1,n2):
        if (abs(n1-n2) < EPSILON):
            return True
        else:
            return False 
    
    def __eq__(self, o):
        if (self.equal(self.x, o.x) and self.equal(self.y, o.y) and self.equal(self.z, o.z) and self.equal(self.w, o.w)):
            return True
        return False

    
    def magnitude(self):
        magnitude = sqrt(self.x**2 + self.y**2 + self.z**2 + self.w**2)
        return magnitude
    
    def normalize(self):
        magnitude = self.magnitude()
        normal = Tuples(self.x / magnitude, self.y / magnitude, self.z / magnitude, self.w / magnitude)
        return normal
    
    def dot(self,o1):
        dot = o1.x*self.x + o1.y*self.y + o1.z*self.z + o1.w*self.w
        return dot

    def cross(self,o1):
        cross = Tuples(self.y*o1.z  - self.z*o1.y , self.z*o1.x - self.x*o1.z, self.x*o1.y - self.y*o1.x )
        return cross

    def reflect(self,other):
        return self - other * 2 * self.dot(other)
    
    def isVector(self):
        return self.w == 0
    
    def isPoint(self):
        return self.w == 1 
    
    def __str__(self) -> str:
        return "X: " + str(self.x) + " Y: " + str(self.y) + " Z: " + str(self.z) + " W: " + str(self.w) 