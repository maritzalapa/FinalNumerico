from math import *
from numpy import *	
import copy


class potencia_inversa():

    def __init__(self,n,AA,xx):
        aa = copy.deepcopy(AA)
        x = copy.deepcopy(xx)
        B = []
        for i in range(n):
            B.append([])
            for j in range(n):
                B[i].append(float(1.0))
        A = dot(0.85,aa)+dot(0.15*(float(1)/float(n)),B)
        self.txt = self.PotenciaInversa(A,x,1e-5,200)
    
    def getmyTxt(self):
        return self.txt

    def PotenciaInversa(self,A,x,tol,NMAX):
	    k=1
	    res=0.0	
	    text='k\t lamda\t\t\t\tx\n'
        
	    A= linalg.inv(A) ###inversa de la matriz A
	    print A
	    y=dot(A,x) 					##siguiente potencia
	    l_ant=linalg.norm(y, inf)	
	    x = [i/l_ant for i in y]
	
	    while k<NMAX :
		    y=dot(A,x) 					##siguiente potencia
		    l=linalg.norm(y, inf)
		    if l==0:
			    text+="ERROR: DIVISION ENTRE CERO!!"	
			    break
		    x = [i/l for i in y]		##normalizacion

		    text+="%d\t%.6f\t"%(k,l)
		    text+= str(x) +"\n"
		    if ( fabs(l-l_ant) <tol ):		
			    print "fin\n"
			    break
		    else:
			    l_ant=l
		    k+=1
	    if k!=NMAX:
	        text+= "\n\nY la solucion final es:\nEigenvalor = "+str(l)+"\nEigenvector = "+str(x)+"\n\n"
	    if k==NMAX:
		    text+="ERROS: FIN DE ITERACIONES  :/"
	    return text
	
