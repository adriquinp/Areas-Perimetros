from Punto import *
from Figuras import *
class Cuadrado(Figuras):
    
    def areaCu(self):
        p3=Punto()
        p3.x=self.p1.x
        p3.y=self.p2.y
        self.area=p3.Distancia(self.p1)*p3.Distancia(self.p1)
    
    def perimetroCu(self):
        p3=Punto()
        p3.x=self.p1.x
        p3.y=self.p2.y
        self.perimetro=4*p3.Distancia(self.p1)
