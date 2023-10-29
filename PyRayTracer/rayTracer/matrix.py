EPSILON = 0.00001
from rayTracer.tuples import Tuples

class Matrix:
    def __init__(self,w,h) -> None:
        self.mat = [[0 for x in range(w)] for y in range(h)]
        self.w = w
        self.h = h
    
    def equal(self,n1,n2):
        if (abs(n1-n2) < EPSILON):
            return True
        else:
            return False
    
    def __eq__(self, __value: object) -> bool:
        eq = True
        if isinstance(__value,Matrix):
             for i in range(self.w):
                for j in range(self.h):
                    if(not self.equal(self.mat[i][j], __value.mat[i][j])):
                        eq = False
                        break
                if eq is False:
                    break
        else:
            for i in range(self.w):
                for j in range(self.h):
                    if(not self.equal(self.mat[i][j], __value.mat.mat[i][j])):
                        eq = False
                        break
                if eq is False:
                    break
        return eq
    
    def __mul__(self, __value: object):
        if (isinstance(__value,Matrix)):
            newMatrix = Matrix(self.w,__value.h)
            newMatrix.mat = [[sum(a * b for a, b in zip(self_row, value_col)) 
                                for value_col in zip(*__value.mat)]
                                    for self_row in self.mat]
        elif(isinstance(__value,Tuples)):
            tupla = []
            tupla.append(__value.x)
            tupla.append(__value.y)
            tupla.append(__value.z)
            tupla.append(__value.w)
            resul = [sum(a * b for a, b in zip(self_row, tupla))
                                    for self_row in self.mat]
            newMatrix = Tuples(resul[0],resul[1],resul[2],resul[3])
        elif(isinstance(__value,(int,float))):
            newMatrix = Matrix(self.w,self.h)
            for i in range(self.w):
                for j in range(self.h):
                    newMatrix.mat[i][j] = self.mat[i][j]*__value
        return newMatrix
    
    def __truediv__(self,__value: object):
        newMatrix = Matrix(self.w,self.h)
        for i in range(self.w):
            for j in range(self.h):
                newMatrix.mat[i][j] = self.mat[i][j] / __value
        return newMatrix
    
    def __rmul__(self,__value: object):        
        return self.__mul__(__value)
    
    def identity(self):
        identidad = Matrix(self.w,self.h)
        for i in range(identidad.w):
            identidad.mat[i][i] = 1
        return identidad
    def transposing(self):
        newMatrix = Matrix(self.w,self.h)
        for i in range(self.w):
            for j in range(self.h):
                newMatrix.mat[i][j] = self.mat[j][i]
        return newMatrix
    
    def determinant(self):
        if self.w != self.h:
            return 0
        elif self.w == 2:
            return self.mat[0][0]*self.mat[1][1] - self.mat[0][1]*self.mat[1][0]
        else:
            determinante = 0
            for col in range(self.w):
                determinante += self.mat[0][col] * self.cofactor(0,col)
            return determinante
    
    def submatrix(self,row,col):
        newMatrix = Matrix(self.w-1,self.h-1)
        countRow =  0
        for i in range(self.w):
            if i == row:
                continue
            countCol = 0
            for j in range(self.h):
                if j == col:
                    continue
                newMatrix.mat[countRow][countCol] = self.mat[i][j]
                countCol += 1
            countRow += 1
        return newMatrix
    
    def minor(self,row,col):
        newMatrix = self.submatrix(row,col)
        return newMatrix.determinant()
    
    def cofactor(self,row,col):
        cof = self.minor(row,col)
        if (row + col) % 2 == 0:
            return cof
        else:
            return -cof
        
    def is_invertible(self):
        if self.determinant() == 0:
            return False
        else:
            return True
        
    def inverse(self):
        det = self.determinant()
        if det == 0:
            return Matrix(0,0)
        else:
            newMatrix = Matrix(self.w,self.h)
            for i in range(self.w):
                for j in range(self.h):
                    newMatrix.mat[i][j] = (self.cofactor(j,i) /det)
            return newMatrix
        
    def __str__(self) -> str:
        return self.mat.__str__()