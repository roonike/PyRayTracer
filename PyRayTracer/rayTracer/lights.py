from rayTracer.colors import Colors
from rayTracer.tuples import Tuples
from math import floor

class Lights:
    def __init__(self,position = Tuples().Point(0, 0, 0),intensity = Colors(1, 1, 1)) -> None:
        self.position = position
        self.intensity = intensity
    
    def __eq__(self,o):
        return self.intensity == o.intensity and self.position == o.position
    
    def point_light(self,position,intensity):
        self.position = position
        self.intensity = intensity
        
    def lighting(self,m, object, light, position, eyev, normalv,in_shadow):
        if m.pattern.declared == True:
            color = m.pattern.pattern_at_object(object,position)
        else:
            color = m.color
            
        if in_shadow is True:
            effectiveColor = color * light.intensity
            ambient = effectiveColor * m.ambient
            return ambient
        else:        
            lightv = tuple()
            effectiveColor = color * light.intensity
            ambient = effectiveColor * m.ambient
            lightv = (light.position - position).normalize()
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
    

