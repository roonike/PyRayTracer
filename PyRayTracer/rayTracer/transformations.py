from rayTracer.matrix import Matrix
import math



class Transformations:
    def __init__(self) -> None:
        self.matrix = Matrix(4,4)
        pass
    
    def translation(self,x,y,z):
        self.matrix.mat[0][0] = self.matrix.mat[1][1] = self.matrix.mat[2][2] = self.matrix.mat[3][3] = 1
        self.matrix.mat[0][3] = x
        self.matrix.mat[1][3] = y
        self.matrix.mat[2][3] = z
        return self.matrix
    
    def scaling(self,x,y,z):
        self.matrix.mat[0][0] = x
        self.matrix.mat[1][1] = y
        self.matrix.mat[2][2] = z
        self.matrix.mat[3][3] = 1
        return self.matrix
    
    def rotation_x(self,r):
        self.matrix.mat[0][0] = 1
        self.matrix.mat[3][3] = 1
        self.matrix.mat[1][1] = self.matrix.mat[2][2] = math.cos(r)
        self.matrix.mat[1][2] = -math.sin(r)
        self.matrix.mat[2][1] = math.sin(r)
        return self.matrix
    
    def rotation_y(self,r):
        self.matrix.mat[1][1] = self.matrix.mat[3][3] = 1
        self.matrix.mat[0][0] = self.matrix.mat[2][2] = math.cos(r)
        self.matrix.mat[2][0] = -math.sin(r)
        self.matrix.mat[0][2] = math.sin(r)
        return self.matrix
    
    def rotation_z(self,r):
        self.matrix.mat[2][2] = self.matrix.mat[3][3] = 1
        self.matrix.mat[0][0] = self.matrix.mat[1][1] = math.cos(r)
        self.matrix.mat[0][1] = -math.sin(r)
        self.matrix.mat[1][0] = math.sin(r)
        return self.matrix
    
    def shearing(self,xy,xz,yx,yz,zx,zy):
        self.matrix.mat[0][0] = self.matrix.mat[1][1] = self.matrix.mat[2][2] = self.matrix.mat[3][3] = 1
        self.matrix.mat[0][1] = xy
        self.matrix.mat[0][2] = xz
        self.matrix.mat[1][0] = yx
        self.matrix.mat[1][2] = yz
        self.matrix.mat[2][0] = zx
        self.matrix.mat[2][1] = zy
        return self.matrix
        