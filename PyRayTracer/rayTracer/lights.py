from rayTracer.colors import Colors
from rayTracer.tuples import Tuples

class Lights:
    def __init__(self,position = Tuples().Point(0, 0, 0),intensity = Colors(1, 1, 1)) -> None:
        self.position = position
        self.intensity = intensity
    
    def __eq__(self,o):
        return self.intensity == o.intensity and self.position == o.position
    
    def point_light(self,position,intensity):
        self.position = position
        self.intensity = intensity
        
    def lighting(self,m, light, position, eyev, normalv,in_shadow = False):
        ambient = diffuse = specular = Colors(1,1,1)
        lightv = tuple()
        effectiveColor = m.color * light.intensity
        lightv = (light.position - position).normalize()
        ambient = effectiveColor * m.ambient
        light_dot_normal = lightv.dot(normalv)
        if(light_dot_normal < 0):
            diffuse = specular = Colors(0,0,0)
        else:
            diffuse = effectiveColor * m.diffuse * light_dot_normal
            
            reflectv = -lightv.reflect(normalv)
            reflect_dot_eye = reflectv.dot(eyev)
            
            if reflect_dot_eye < 0:
                specular = Colors(0,0,0)
                
            else:
                factor = pow(reflect_dot_eye, m.shininess)
                specular = light.intensity * m.specular * factor
        return ambient + diffuse + specular
    