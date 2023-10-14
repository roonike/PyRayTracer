
from rayTracer.tuples import Tuples

class Matrix:
    def __init__(self,i,j) -> None:
        self.mat = [[0 for x in range(i)] for y in range(j)] 
        self.w = i
        self.h = j
        pass
    
    def __eq__(self, __value: object) -> bool:
        eq = True
        for i in range(self.w):
            for j in range(self.h):
                if(self.mat[i][j] != __value.mat[i][j]):
                    eq = False
                    break
            if eq is False:
                break
        return eq;    
    
    def __mul__(self, __value: object):
        if (isinstance(__value,Matrix)):
            newMatrix = Matrix(self.w,__value.h)
            newMatrix.mat = [[sum(a * b for a, b in zip(self_row, value_col)) 
                                for value_col in zip(*__value.mat)]
                                    for self_row in self.mat]
        elif(isinstance(__value,Tuples)):
            newMatrix = Matrix(self.w, 4)
        return newMatrix
    
    