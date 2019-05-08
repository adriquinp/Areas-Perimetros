# -*- coding: utf-8 -*-
import tkinter as tk
from Figuras import *
from Punto import *
from Rectangulo import *
from Circulo import *
from Triangulo import *
from Cuadrado import *



root = tk.Tk()
etiquetax1 = tk.Label(root, text="Ingrese la coordenada en x del primer punto:").grid(row=0, column=1)

coord_x1 = tk.IntVar()
coordenada_x1 = tk.Entry(root,textvariable=coord_x1)
coordenada_x1.grid(row=1, column=1)

etiquetay1 = tk.Label(root, text="Ingresa la coordenada en y del primer punto:")
etiquetay1.grid(row=0, column=3)
coord_y1 = tk.IntVar()
coordenada_y1 = tk.Entry(root,textvariable=coord_y1)

coordenada_y1.grid(row=1, column=3)

etiquetax2 = tk.Label(root, text="Ingrese la coordenada en x del segundo punto:")
etiquetax2.grid(row=2, column=1)
coord_x2 = tk.IntVar()
coordenada_x2 = tk.Entry(root,textvariable=coord_x2)
coordenada_x2.grid(row=3, column=1)
etiquetay2 = tk.Label(root, text="Ingresa la coordenada en y del segundo punto:")
etiquetay2.grid(row=2, column=3)
coord_y2 = tk.IntVar()
coordenada_y2 = tk.Entry(root,textvariable=coord_y2)

coordenada_y2.grid(row=3, column=3)
etiquetaSel = tk.Label(root, text="Seleccione la figura geométrica:")
etiquetaSel.grid(row=4,column=2)
variable = tk.StringVar()
radiobutton1 = tk.Radiobutton(text="Cuadrado", variable=variable, value=1)
radiobutton2 = tk.Radiobutton(text="Círculo", variable=variable, value=2)
radiobutton3 = tk.Radiobutton(text="Triángulo", variable=variable, value=3)
radiobutton4 = tk.Radiobutton(text="Rectángulo", variable=variable, value=4)
radiobutton1.grid(row=5, column=1)
radiobutton2.grid(row=5, column=3)
radiobutton3.grid(row=6, column=1)
radiobutton4.grid(row=6, column=3)

def funcionArea():
    p = Punto()
    p.x = coord_x1.get()
    p.y = coord_y1.get()
    q = Punto()
    q.x = coord_x2.get()
    q.y = coord_y2.get()
    rta = 0.0
    tip = ""
    if variable.get()=="4":
        f = Rectangulo()
        f.setPuntos(p, q)
        f.areaR()
        rta = f.area
        tip = "rectángulo"
    elif variable.get()=="3":
        f = Triangulo()
        f.setPuntos(p, q)
        f.areat()
        rta = f.area
        tip = "triángulo"
    elif variable.get()=="2":
        f = Circulo()
        f.setPuntos(p, q)
        f.areac()
        rta = f.area
        tip = "círculo"
    else:
        f = Cuadrado()
        f.setPuntos(p, q)
        f.areaCu()
        rta = f.area
        tip = "cuadrado"
    respuesta = tk.Label(root, text="El área del " + tip + " es " + str(rta))
    respuesta.grid(row=9,column=2)
botonArea = tk.Button(root, text="Calcular área",command=funcionArea)

botonArea.grid(row=7, column=2)
def funcionPerimetro():
    p = Punto()
    p.x = coord_x1.get()
    p.y = coord_y1.get()
    q = Punto()
    q.x = coord_x2.get()
    q.y = coord_y2.get()
    rta=0.0
    tip=""

    if variable.get()=="4":
        f = Rectangulo()
        f.setPuntos(p, q)
        f.perimetror()
        rta = f.perimetro
        tip="rectángulo"


    elif variable.get()=="3":
        f = Triangulo()
        f.setPuntos(p, q)
        f.perimetroTri()
        rta = f.perimetro
        tip = "triángulo"
    elif variable.get()=="2":
        f = Circulo()
        f.setPuntos(p, q)
        f.perimetroc()
        rta = f.perimetro
        tip = "círculo"
    else:
        f = Cuadrado()
        f.setPuntos(p, q)
        f.perimetroCu()
        rta = f.perimetro
        tip = "cuadrado"
    respuesta = tk.Label(root, text="El perímetro del " + tip + " es " + str(rta))
    respuesta.grid(row=10,column=2)

botonPerimetro = tk.Button(root, text="Calcular perímetro",command=funcionPerimetro)
botonPerimetro.grid(row=8, column=2)


root.mainloop()
