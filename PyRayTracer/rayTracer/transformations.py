from rayTracer.matrix import Matrix
import math



class Transformations:
    @staticmethod
    def translation(x,y,z):
        mat = Matrix(4,4).identity()
        mat.mat[0][3] = x
        mat.mat[1][3] = y
        mat.mat[2][3] = z
        return mat
    
    @staticmethod
    def scaling(x,y,z):
        mat = Matrix(4,4).identity()
        mat.mat[0][0] = x
        mat.mat[1][1] = y
        mat.mat[2][2] = z
        return mat
    
    @staticmethod
    def rotation_x(r):
        mat = Matrix(4,4).identity()
        mat.mat[1][1] = mat.mat[2][2] = math.cos(r)
        mat.mat[1][2] = -math.sin(r)
        mat.mat[2][1] = math.sin(r)
        return mat
    
    @staticmethod
    def rotation_y(r):
        mat = Matrix(4,4).identity()
        mat.mat[0][0] = mat.mat[2][2] = math.cos(r)
        mat.mat[2][0] = -math.sin(r)
        mat.mat[0][2] = math.sin(r)
        return mat
    
    @staticmethod
    def rotation_z(r):
        mat = Matrix(4,4).identity()
        mat.mat[0][0] = mat.mat[1][1] = math.cos(r)
        mat.mat[0][1] = -math.sin(r)
        mat.mat[1][0] = math.sin(r)
        return mat
    
    @staticmethod
    def shearing(xy,xz,yx,yz,zx,zy):
        mat = Matrix(4,4).identity()
        mat.mat[0][1] = xy
        mat.mat[0][2] = xz
        mat.mat[1][0] = yx
        mat.mat[1][2] = yz
        mat.mat[2][0] = zx
        mat.mat[2][1] = zy
        return mat
        