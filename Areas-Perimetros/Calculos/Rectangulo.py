from Punto import *
from Figuras import *
class Rectangulo(Figuras):
    
    def areaR(self):
        p3=Punto()
        p3.x=self.p1.x
        p3.y=self.p2.y
        self.area=p3.Distancia(self.p1)*p3.Distancia(self.p2)
    
    def perimetror(self):
        p3=Punto()
        p3.x=self.p1.x
        p3.y=self.p2.y
        self.perimetro=2*p3.Distancia(self.p1)+2*p3.Distancia(self.p2)
