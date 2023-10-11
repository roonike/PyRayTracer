EPSILON = 0.00001

class Colors:
    def __init__(self,R,G,B) -> None:
        self.r = R
        self.g = G
        self.b = B
        pass

    def equal(self,n1,n2):
        if (abs(n1-n2) < EPSILON):
            return True
        else:
            return False 
        
    def __eq__(self, o):
        if (self.equal(self.r, o.r) and self.equal(self.g, o.g) and self.equal(self.b, o.b)):
            return True
        return False
    
    def __add__(self,o):
        newC = Colors(self.r + o.r, self.g + o.g, self.b + o.b)
        return newC 
    
    
    def __sub__(self,o):
        newC = Colors(self.r - o.r, self.g - o.g, self.b - o.b)
        return newC 
        
    def __mul__(self,o):
        if isinstance(o,(float,int)):
            newC = Colors(self.r * o, self.g * o, self.b * o)
            return newC
        elif isinstance(o,Colors):
            newC = Colors(self.r * o.r, self.g * o.g, self.b * o.b)
            return newC
    
    def __rmul__(self,o):
        if isinstance(float,int):
            newC = Colors(self.r * o, self.g * o, self.b * o)
            return newC
        elif isinstance(Colors):
            newC = Colors(self.r * o.r, self.g * o.g, self.b * o.b)
            return newC

