from rayTracer.transformations import Transformations
from rayTracer.matrix import Matrix
class Camera:
    def __init__(self,hsize,vsize,field_of_view) -> None:
        self.hsize = hsize
        self.vsize = vsize
        self.field_of_view = field_of_view
        self.transform = Matrix(4,4).identity()