import math
import copy

class Matrix:
    def __init__(self, A):
        self.A = copy.deepcopy(A)
        m = len(self.A)
        n = len(self.A[0])
    
    
    #def constructWithCopy(): #linea 155
    
    def copy():
        X = [ [0.0 for i in range(n)] for j in range(m)]
            
    def transpose(self):
        At = [ [0.0 for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n):
                At[i][j] = self.A[j][i]
        return At
    
    def norm1(self):
        f = 0.0
        for j in range(n):
            s = 0.0
            for i in range(n):
                s+= math.fabs(self.A[i][j]);
            f = max(s, f)
        return f
        
    def uminus(self):
        mA = [ [0.0 for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n):
                mA = (-1.0)*self.A[i][j]
        return mA
    
    def plus(self, B):
        C = [ [0.0 for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n):
                C[i][j] = self.A[i][j]+B[i][j]
        return C
    
    def plusEquals(self, B):
        for i in range(n):
            for j in range(n):
                self.A[i][j] = self.A[i][j]+B[i][j]
        return self.A
    
                
