import sys
from Tkinter import *
from Biseccion import *
from RegulaFalsi import *
from numpy import linspace
from NewtonRaphson import *
from Secante import *
from PuntoFijo import *
from PuntoFijoAitken import *
from PuntoFijoSteffensen import *
from PicardJacobi import *
from PicardSeidel import *
from NewtonsRaphsonMatriz import *
from matplotlib.pyplot import plot,figure,grid,show
import tkMessageBox
import os
import copy
import numpy
import math

mGui = Tk()
mynumA = DoubleVar()
mynumB = DoubleVar()
myfun = StringVar()
pointSystem = StringVar()
constSystem = StringVar()
A = []

def mabout():
    texto = '5ta Tarea\nAnalisis Numerico\n2014-1'
    tkMessageBox.showinfo('Que es esto?', texto)
    
def creditos():
    texto = 'Jesus Lovon Melgarejo\nMaritza Lapa Romero\n'
    tkMessageBox.showinfo('Desarrollado por:', texto)

def biseccion():
    
    fun = myfun.get()
    myA = mynumA.get()
    myB = mynumB.get()
    b = Biseccion(fun,myA,myB)
    txt = b.getmyTxt()
    f=open("biseccion.txt",'w+')
    f.write(txt)
    f.close()
    os.system('gedit biseccion.txt')


def falsi():
    fun = myfun.get()
    myA = mynumA.get()
    myB = mynumB.get()
    b = RegulaFalsi(fun,myA,myB)
    txt = b.getmyTxt()
    f=open("Rfalsi.txt",'w+')
    f.write(txt)
    f.close()
    os.system('gedit Rfalsi.txt')


    
def raphson():
    fun = myfun.get()
    myA = mynumA.get()
    myB = mynumB.get()
    b = NewtonRaphson(fun,myA,myB)
    txt = b.getmyTxt()
    f=open("NRaphson.txt",'w+')
    f.write(txt)
    f.close()
    os.system('gedit NRaphson.txt')
    
def pfijo():
    fun = myfun.get()
    myA = mynumA.get()
    myB = mynumB.get()
    b = PuntoFijo(fun,myA,myB)
    txt = b.getmyTxt()
    f=open("PFijo.txt",'w+')
    f.write(txt)
    f.close()
    os.system('gedit PFijo.txt')

def secante():
    fun = myfun.get()
    myA = mynumA.get()
    myB = mynumB.get()
    b = Secante(fun,myA,myB)
    txt = b.getmyTxt()
    f=open("secante.txt",'w+')
    f.write(txt)
    f.close()
    os.system('gedit secante.txt')

def steffensen():
    fun = myfun.get()
    myA = mynumA.get()
    myB = mynumB.get()
    b = PuntoFijoSteffensen(fun,myA,myB)
    txt = b.getmyTxt()
    f=open("PFijoSteffensen.txt",'w+')
    f.write(txt)
    f.close()
    os.system('gedit PFijoSteffensen.txt')
    
def aitken():
    fun = myfun.get()
    myA = mynumA.get()
    myB = mynumB.get()
    b = PuntoFijoAitken(fun,myA,myB)
    txt = b.getmyTxt()
    f=open("PFijoAitken.txt",'w+')
    f.write(txt)
    f.close()
    os.system('gedit PFijoAitken.txt')

def picardJacobi():
    global A
    readMatrix()
    point = pointSystem.get()
    points = point.split(' ')
    x = []
    
    const = constSystem.get()
    consts = const.split(' ')
    c = []
    if consts[0]=='':
        tkMessageBox.showinfo("Error", "Debe ingresar constantes")
        return
    for i in range(len(consts)):
        c.append(float(consts[i]))
    
    if points[0]=='':
        #definir un rango defecto y buscar soluciones, como en las funciones anteriores
        #x = [0.5,1.5]
        x = None
    else:
        for i in range(len(points)):
            x.append(float(points[i]))
    pj = PicardJacobi(A,x,c)
    txt = pj.getmyTxt()
    txt = txt.replace('[','(')
    txt = txt.replace(']',')')
    f=open("PiccardJacobi.txt",'w+')
    if len(txt)<5:
        f.write("Diverge escoger otros valores de u, v para mejorar la convergencia")
    else:
        f.write(txt)
    f.close()
    os.system('gedit PiccardJacobi.txt')
    
def picardSeidel():
    global A
    readMatrix()
    point = pointSystem.get()
    points = point.split(' ')
    x = []
    
    const = constSystem.get()
    consts = const.split(' ')
    c = []
    if consts[0]=='':
        tkMessageBox.showinfo("Error", "Debe ingresar constantes")
        return
    if len(consts)>2:
        tkMessageBox.showinfo("Error", "Solo definido para sistema 2x2")
        return
    for i in range(len(consts)):
        c.append(float(consts[i]))
    
    if points[0]=='':
        #definir un rango defecto y buscar soluciones, como en las funciones anteriores
        x = None
    else:
        for i in range(len(points)):
            x.append(float(points[i]))
    ps = PicardSeidel(A,x,c)
    txt = ps.getmyTxt()
    txt = txt.replace('[','(')
    txt = txt.replace(']',')')
    f=open("PiccardSeidel.txt",'w+')
    if len(txt)<5:
        f.write("Diverge escoger otros valores de u, v para mejorar la convergencia")
    else:
        f.write(txt)
    f.close()
    os.system('gedit PiccardSeidel.txt')
    
def raphsonMatrix():
    global A
    readMatrix()
    point = pointSystem.get()
    points = point.split(' ')
    x = []
    if points[0]=='':
        #definir un rango defecto y buscar soluciones, como en las funciones anteriores
        x = None
    else:
        for i in range(len(points)):
            x.append(float(points[i]))
    rm = RaphsonMatrix(A,x)
    txt = rm.getmyTxt()
    txt = txt.replace('[','(')
    txt = txt.replace(']',')')
    f=open("RaphsonMatrix.txt",'w+')
    f.write(txt)
    f.close()
    os.system('gedit RaphsonMatrix.txt')

def evaluateX(Q,str_function):
    res = []
    ns = vars(math).copy()
    ns['__builtins__'] = None
    for q in Q:
        new_fun = ''
        new_fun = copy.deepcopy(str_function)
        new_fun = new_fun.replace('x','('+str(q)+')')
        new_fun = new_fun.replace('^','**')    
        res.append(eval(new_fun,ns))
    return res

def plotear():
    fun = myfun.get()
    myA = mynumA.get()
    myB = mynumB.get()
    if myA==0.0 and myB==0.0:
        myA=-100.0
        myB=100.0
    x = linspace(myA, myB, 400)
    y = evaluateX(x,fun)
    figure()
    plot(x,y)
    grid(True)
    show()

def inputA():
    os.system("gedit matrizA.txt")
    
def readMatrix():
    global A
    A = []
    f=open("matrizA.txt",'r+')
    while(1):
        line = f.readline()
        if not line:
            break
        A.append(line)    
        
def main():
    #mGui = Tk()
    mGui.geometry('500x420+200+200')
    mGui.title('Solucion Sistemas No Lineales')
    label1 = Label(mGui,text='Ingrese la funcion F(x)').place(x=20,y=20)
    mtextNum = Entry(mGui, textvariable = myfun).place(x=20,y=40)
    label2 = Label(mGui,text='Ingrese el intervalo').place(x=20,y=60)
    mtextNum = Entry(mGui, textvariable = mynumA).place(x=20,y=80)
    mtextNum = Entry(mGui, textvariable = mynumB).place(x=80,y=80)
    mbotonPlot = Button(mGui, text = 'Plotear funcion', command = plotear).place(x=20, y = 100)  
    mbotonBiseccion = Button(mGui, text = 'Biseccion', command = biseccion).place(x=20, y = 140)
    mbotonFalsi = Button(mGui, text = 'Regula Falsi', command = falsi).place(x=20,y=180)
    mbotonRaphson = Button(mGui, text = 'Newton-Raphson', command = raphson).place(x=20,y=220)
    mbotonPfijo = Button(mGui, text = 'Punto Fijo', command = pfijo).place(x=20,y=260)
    mbotonSecante = Button(mGui, text = 'Secante', command = secante).place(x=20,y=300)
    mbotonSteffensen = Button(mGui, text = 'Steffensen', command = steffensen).place(x=20,y=340)
    mbotonAitken = Button(mGui, text = 'Aitken', command = aitken).place(x=20,y=380)
    label3 = Label(mGui,text='Sistema de ecuaciones no lineales').place(x=250,y=20)
    mbotonmatriA = Button(mGui,text='Ingrese matriz de ecuaciones',command=inputA).place(x=250,y=40)
    label4 = Label(mGui,text='Punto referencial').place(x=250,y=80)
    mtextPoint = Entry(mGui, textvariable = pointSystem).place(x=250,y=100)
    label4 = Label(mGui,text='Constantes para Picard (u,v,...)').place(x=250,y=140)
    mtextConst = Entry(mGui, textvariable = constSystem).place(x=250,y=160)
    mbotonPicardJacobi = Button(mGui,text='Picard-Jacobi',command = picardJacobi).place(x=250,y=200)
    mbotonPicardSeidel = Button(mGui,text='Picard-Seidel', command = picardSeidel).place(x=250,y=240)
    mbotonNewtonRaphson = Button(mGui, text='Newton Raphson', command = raphsonMatrix).place(x=250,y=280)
    #MENU
    menubar = Menu(mGui)
    filemenu = Menu(menubar,tearoff=0)
    filemenu.add_command(label='About', command =mabout)
    filemenu.add_command(label='Creditos',command = creditos)
    menubar.add_cascade(labe= 'Help',menu=filemenu)
    mGui.config(menu = menubar)
        
    mGui.mainloop()

if __name__ == "__main__":
    main()
