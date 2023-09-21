class Color:
    def __init__(self,R,G,B,W = 0) -> None:
        self.r = R
        self.g = G
        self.b = B
        self.w = W
        pass

    def __eq__(self, o):
        return (self.r == o.r and self.g == o.g and self.b == o.b )

    def __add__(self,o):
        newC = Color(self.r + o.r, self.g + o.g, self.b + o.b)
        return newC 
    
    def __sub__(self,o):
        newC = Color(self.r - o.r, self.g - o.g, self.b - o.b)
        return newC 
        
    def __mul__(self,o):
        if isinstance(float,int):
            newC = Color(self.r * o, self.g * o, self.b * o)
            return newC
        elif isinstance(Color):
            newC = Color(self.r * o.r, self.g * o.g, self.b * o.b)
    
    def __rmul__(self,o):
        if isinstance(float,int):
            newC = Color(self.r * o, self.g * o, self.b * o)
            return newC
        elif isinstance(Color):
            newC = Color(self.r * o.r, self.g * o.g, self.b * o.b)

