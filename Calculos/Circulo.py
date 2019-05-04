from Punto import *
from Figuras import *
import math
class Circulo(Figuras):
    
    def areac(self):
       
        self.area=math.pi*(self.p1.Distancia(self.p2))**2

    def perimetroc(self):
       
        self.perimetro=2*math.pi*(self.p1.Distancia(self.p2))
    
