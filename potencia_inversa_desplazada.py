from math import *
from numpy import *
import copy

class potencia_inversa_desplazada():
    
    def __init__(self,n,AA,xx,desp=1.5,rho=0.15):
        print desp, n
        aa = copy.deepcopy(AA)
        x = copy.deepcopy(xx)
        B = []
        for i in range(n):
            B.append([])
            for j in range(n):
                B[i].append(float(1.0))
        A = dot(1.0-rho,aa)+dot(rho*(float(1)/float(n)),B)
        print A
        self.txt = self.PotenciaInversaDesplazada(A,x,1e-5,200,desp)
    
    def getmyTxt(self):
        return self.txt
  
    def PotenciaInversaDesplazada(self,A,x,tol,NMAX,lam):
	    k=1
	    res=0.0	
	    text='k\t lamda\t\t\t\tx\n'
	    for i in range(len(A)):
		    A[i][i]-=lam
	
	    A= linalg.inv(A) ###inversa de la matriz A
	    y=dot(A,x) 					##siguiente potencia
	    l_ant=linalg.norm(y, inf)	
	    x = [i/l_ant for i in y]
		
	    while k<NMAX :
		    y=dot(A,x) 					##siguiente potencia
		    l=linalg.norm(y, inf)
		    x = [i/l for i in y]		##normalizacion

		    text+="%d\t%.6f\t"%(k,l)
		    text+= str(x) +"\n"
		    if ( fabs(l-l_ant) <tol ):		
			    print "fin\n"
			    break
		    else:
			    l_ant=l
		    k+=1
		    if l==0:
			    text+="ERROR: DIVISION ENTRE CERO!!"	
			    break
	    if k!=NMAX:
	        text+= "\n\nY la solucion final es:\nEigenValor = "+str(l)+"\nEigenvector = "+str(x)+"\n\n"
	    if k==NMAX:
		    text+="ERROS: FIN DE ITERACIONES  :/"
	    return text
	    
	    
