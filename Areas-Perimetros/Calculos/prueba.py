from Punto import *
from Rectangulo import *
from Circulo import *
from Triangulo import *
from Cuadrado import *

p1=Punto()
p2=Punto()
p1.x=input("Ingrese la coordenada en x del primer punto: ")
p1.y=input("Ingrese la coordenada en y del primer punto: ")
p2.x=input("Ingrese la coordenada en x del segundo punto: ")
p2.y=input("Ingrese la coordenada en y del segundo punto: ")


r=Rectangulo()
r.setPuntos(p1,p2)
r.areaR()
r.perimetror()

c=Circulo()
c.setPuntos(p1,p2)
c.areac()
c.perimetroc()


t=Triangulo()
t.setPuntos(p1,p2)
t.areat()
t.perimetrot()

cu=Cuadrado()
cu.setPuntos(p1,p2)
cu.areaCu()
cu.perimetroCu()

areas = [str(r.area), str(c.area),str(t.area),str(cu.area)]
perimetros=[ str(r.perimetro),str(c.perimetro),str(t.perimetro),str(cu.perimetro)]
variables = ['rectángulo', 'círculo','triángulo','cuadrado']
for variables, areas, perimetros in zip(variables,areas, perimetros) :
    print ' El área y perímetro de tu {} son: {} y {}'.format(variables, areas, perimetros)



