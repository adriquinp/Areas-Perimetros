# -*- coding: utf-8 -*-
import Tkinter as tk
from Figuras import *
from Punto import *
from Rectangulo import *
from Circulo import *
from Triangulo import *
from Cuadrado import *


root = tk.Tk()
etiquetax1 = tk.Label(root, text="Ingrese la coordenada en x del primer punto:")
etiquetax1.pack()
coord_x1 = tk.IntVar()
coordenada_x1 = tk.Entry(root,textvariable=coord_x1)
etiquetay1 = tk.Label(root, text="Ingresa la coordenada en y del primer punto:")
etiquetay1.pack()
coord_y1 = tk.IntVar()
coordenada_y1 = tk.Entry(root,textvariable=coord_y1)
coordenada_x1.pack()
coordenada_y1.pack()

etiquetax2 = tk.Label(root, text="Ingrese la coordenada en x del segundo punto:")
etiquetax2.pack()
coord_x2 = tk.IntVar()
coordenada_x2 = tk.Entry(root,textvariable=coord_x2)
etiquetay2 = tk.Label(root, text="Ingresa la coordenada en y del segundo punto:")
etiquetay2.pack()
coord_y2 = tk.IntVar()
coordenada_y2 = tk.Entry(root,textvariable=coord_y2)
coordenada_x2.pack()
coordenada_y2.pack()
etiquetaSel = tk.Label(root, text="Seleccione la figura geométrica:")
etiquetaSel.pack()
variable = tk.StringVar()
radiobutton1 = tk.Radiobutton(text="Cuadrado", variable=variable, value=1)
radiobutton2 = tk.Radiobutton(text="Círculo", variable=variable, value=2)
radiobutton3 = tk.Radiobutton(text="Triángulo", variable=variable, value=3)
radiobutton4 = tk.Radiobutton(text="Rectángulo", variable=variable, value=4)
radiobutton1.pack()
radiobutton2.pack()
radiobutton3.pack()
radiobutton4.pack()

def funcionArea():
    p = Punto()
    p.x = coord_x1.get()
    p.y = coord_y1.get()
    q = Punto()
    q.x = coord_x2.get()
    q.y = coord_y2.get()
    if variable.get()=="4":
        f = Rectangulo()
        f.setPuntos(p, q)
        f.areaR()
        print "El área del  rectángulo es: " + str(f.area)
    elif variable.get()=="3":
        f = Triangulo()
        f.setPuntos(p, q)
        f.areat()
        print "El área del  triángulo es: " + str(f.area)
    elif variable.get()=="2":
        f = Circulo()
        f.setPuntos(p, q)
        f.areac()
        print "El área del  círculo es: " + str(f.area)
    else:
        f = Cuadrado()
        f.setPuntos(p, q)
        f.areaCu()
        print "El área del  cuadrado es: " + str(f.area)
        
botonArea = tk.Button(root, text="Calcular área",command=funcionArea)

botonArea.pack()
def funcionPerimetro():
    p = Punto()
    p.x = coord_x1.get()
    p.y = coord_y1.get()
    q = Punto()
    q.x = coord_x2.get()
    q.y = coord_y2.get()
    if variable.get()=="4":
        f = Rectangulo()
        f.setPuntos(p, q)
        f.perimetroR()
        print "El perímetro del rectángulo es: " + str(f.perimetro)
    elif variable.get()=="3":
        f = Triangulo()
        f.setPuntos(p, q)
        f.perimetrot()
        print "El perímetro del triángulo es: " + str(f.perimetro)
    elif variable.get()=="2":
        f = Circulo()
        f.setPuntos(p, q)
        f.perimetroc()
        print "El perímetro del  círculo es: " + str(f.perimetro)
    else:
        f = Cuadrado()
        f.setPuntos(p, q)
        f.perimetroCu()
        print "El perímetro del  cuadrado es: " + str(f.perimetro)

botonPerimetro = tk.Button(root, text="Calcular perímetro",command=funcionPerimetro)
botonPerimetro.pack()


root.mainloop()
