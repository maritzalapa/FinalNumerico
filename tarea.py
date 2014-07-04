import sys
from Tkinter import *
from potencia import *
from potencia_inversa_desplazada import *
from potencia_inversa import *

import tkMessageBox
import os
import copy
import numpy
import math

mGui = Tk()

matrizA = []
matrizX = []
n = 0
myDesp = DoubleVar()
myRho = DoubleVar()

def mabout():
    texto = 'PAGE RANK\n\nProyecto Final\nAnalisis Numerico\n2014-1'
    tkMessageBox.showinfo('Que es esto?', texto)
    
def creditos():
    texto = 'Jesus Lovon Melgarejo\nMaritza Lapa Romero\nAlonso Guillen\nJason Martinez\nGiovanny Mondragon\n'
    tkMessageBox.showinfo('Desarrollado por:', texto)

def getMatrixfromTextA():
    os.system("gedit matrizA.txt")
    
def getMatrixfromTextX():
    os.system("gedit vectorX.txt")

def mPotencia():
    myR = myRho.get()
    if myR == 0.0:
        myR = 0.15
    global n
    global matrizA
    global matrizX
    readMatrizA()
    readMatrizX()
    #print myR
    b = potencia(n,matrizA,matrizX, myR)
    txt = b.getmyTxt()
    f=open("potencia.txt",'w+')
    f.write(txt)
    f.close()
    os.system('gedit potencia.txt')


def mPotenciaInversa():
    global n
    global matrizA
    global matrizX
    readMatrizA()
    readMatrizX()
    myR = myRho.get()
    if myR == 0.0:
        myR = 0.15
    b = potencia_inversa(n,matrizA, matrizX, myR)
    txt = b.getmyTxt()
    f=open("potenciaInversa.txt",'w+')
    f.write(txt)
    f.close()
    os.system('gedit potenciaInversa.txt')


    
def mPotenciaInversaDesplazada():
    global n
    global matrizA
    global matrizX
    readMatrizA()
    readMatrizX()
    myR = myRho.get()
    myD = myDesp.get()
    if myR == 0.0:
        myR = 0.15
    b = potencia_inversa_desplazada(n,matrizA, matrizX, myD, myR)
    txt = b.getmyTxt()
    f=open("PotenciaInversaDesplazada.txt",'w+')
    f.write(txt)
    f.close()
    os.system('gedit PotenciaInversaDesplazada.txt')
    
def mQR():
    b = PuntoFijoAitken(fun,myA,myB)
    txt = b.getmyTxt()
    f=open("PFijoAitken.txt",'w+')
    f.write(txt)
    f.close()
    os.system('gedit PFijoAitken.txt')
    
def readMatrizA():
    global dim
    global n
    global matrizA
    matrizA = []
    f = open("matrizA.txt", 'r+')
    dim = 0
    while(1):
        line = f.readline()
        if not line:
            break
        dim = dim+1
        numrow = line.split()
        ROW = []
        for num in numrow:
            ROW.append(float(num))
        matrizA.append(ROW)
    n = dim        


def readMatrizX():
    global matrizX
    matrizX = []
    f = open("vectorX.txt", 'r+')
    line = f.readline()
    if not line:
        return
    rows = line.split()
    for num in rows:
        matrizX.append(float(num))
    return

def main():
    #mGui = Tk()
    mGui.geometry('500x420+200+200')
    mGui.title('PAGE RANK')
    mbotonMatriz = Button(mGui, text = 'Ingrese la matriz A', command = getMatrixfromTextA).place(x=20,y=20)
    mbotonMatriz2 = Button(mGui, text = 'Ingrese el vector X', command = getMatrixfromTextX).place(x=20,y=60)
    label2 = Label(mGui,text='Ingrese desplazamiento (Solo para metodos que lo usen)').place(x=20,y=100)
    mtextNum = Entry(mGui, textvariable = myDesp).place(x=20,y=120)
    label3 = Label(mGui,text='Ingrese el parametro rho (por defecto 0.15)').place(x=20,y=160)
    mtextNum2 = Entry(mGui, textvariable = myRho).place(x=20,y=180)

    mbotonPotencia = Button(mGui, text = 'Potencia Simple', command = mPotencia).place(x=20, y = 240)
    mbotonPotenciaInversa = Button(mGui, text = 'Potencia Inversa', command = mPotenciaInversa).place(x=20,y=280)
    mbotonPotenciaInversaDesplazada = Button(mGui, text = 'Potencia Inversa con Desplazamiento', command = mPotenciaInversaDesplazada).place(x=20,y=320)
    mbotonQR = Button(mGui, text = 'Metodo QR', command = mQR).place(x=20,y=360)

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

