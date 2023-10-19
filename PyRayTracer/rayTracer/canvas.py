from math import ceil
from rayTracer.colors import Colors
class Canvas:
    def __init__(self,w,h,color = Colors(0,0,0)) -> None:
        self.height = h
        self.width = w
        color = color * 255
        color.r = ceil(color.r)
        color.g = ceil(color.g)
        color.b = ceil(color.b)
        if color.r > 255:
            color.r = 255
        elif color.r < 0:
            color.r = 0
        if color.g> 255:
            color.g = 255
        elif color.g < 0:
            color.g = 0
        if color.b > 255:
            color.b = 255
        elif color.b < 0:
            color.b = 0
        self.canva = [[color for x in range(h)] for y in range(w)]
        pass
    
    def write_pixel(self,x,y,color):
        color = color * 255
        color.r = ceil(color.r)
        color.g = ceil(color.g)
        color.b = ceil(color.b)
        if color.r > 255:
            color.r = 255
        elif color.r < 0:
            color.r = 0
        if color.g> 255:
            color.g = 255
        elif color.g < 0:
            color.g = 0
        if color.b > 255:
            color.b = 255
        elif color.b < 0:
            color.b = 0
        self.canva[x][y] = color
    
    def pixel_at(self,x,y):
        return self.canva[x][y]
    
    def canvas_to_ppm(self,path):
        with open(path,'w') as ppm:
            ppm.write("P3\n")
            ppm.write("{} {}\n".format(self.width,self.height))
            ppm.write("255\n")
            count = 0
            value = ""
            print(self.width * 3)
            for h in range(self.height):
                for w in range(self.width):
                    for color in range(3):
                        if(color == 0):
                            value = str(self.pixel_at(w,h).r)
                        elif(color == 1):
                            value = str(self.pixel_at(w,h).g)
                        elif(color == 2):
                            value = str(self.pixel_at(w,h).b)
                        chars_to_write = len(value)
                        if count + chars_to_write > 70:
                            ppm.write("\n")
                            count = 0
                            ppm.write(value)
                            count += chars_to_write
                        else:
                            ppm.write(value)
                            count += chars_to_write
                        if (count + 1 > 70):
                            ppm.write("\n")
                            count = 0
                        else:
                            ppm.write(" ")
                            count += 1  
                count = 0
                ppm.write("\n")
