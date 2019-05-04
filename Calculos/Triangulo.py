from Punto import *
from Figuras import *
class Triangulo(Figuras):
    
    
    def areat(self):
        p3=Punto()
        p3.x=self.p1.x
        p3.y=self.p2.y
        self.area=p3.Distancia(self.p1)*p3.Distancia(self.p2)/2
    

    def perimetrot(self):
        p3=Punto()
        p3.x=self.p1.x
        p3.y=self.p2.y
        self.perimetro=p3.Distancia(self.p1)+p3.Distancia(self.p2)+self.p1.Distancia(self.p2)
