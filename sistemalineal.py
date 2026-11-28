from matplotlib.pylab import norm
from numpy import zeros, dot, array
import numpy as np

def my_Gauss(A,b):
    N= len(b)
    x=zeros(N)
    for i in range (0,N):
        for k in range (i+1,N):
            c=A[k,i]/A[i,i]
            A[k,:]=A[k,:]-c*A[i,:]
            b[k]=b[k]-b[i]*c
    for i in range(N-1, -1, -1):
        x[i]=(b[i]-dot(A[i,i+1:],x[i+1:]))/A[i,i]
    return x

def my_Jacobi(A,b): 

    N = len(b)
    x, D, R = zeros(N), zeros(N), zeros((N, N))
    xn = 1 + x 
    tolerance = 1e-10
    k, max_iter = 0, 100

  # Jacobi iteration
    for i in range(N): 
     for  j in range(N): 
       if i==j: 
          D[i] = A[i,j]
          R[i,j] = 0 
       else:
          R[i,j] = A[i,j]
   
    while norm(xn - x) > tolerance  and  k < max_iter: 
        x = xn.copy()
        xn = (b - dot(R, x)) / D
        k+=1

    return x 

def my_jacobi(matriz_estatica,vector_cargas):
    N=len(vector_cargas)
    k, max_iter = 0, 100
    X1,X2=np.zeros(N),np.zeros(N)
    Lu = np.zeros((N,N))
    Lu[:,:]= matriz_estatica[:,]
    for i in range(N):
        Lu[i,i]=0
        R= vector_cargas - np.matmul(Lu,X1)
    for i in range(N):
        X2[i]=R[i]/ matriz_estatica[i,i]

    while norm(X2 - X1) > 1e-10 and k < max_iter:
        X1 = X2.copy()          
        R = vector_cargas - np.matmul(Lu, X1)
        for i in range(N):
            X2[i] = R[i] / matriz_estatica[i, i]
        k += 1
    print(X2)
    return X2 

import numpy as np
from numpy.linalg import norm

def my_jacobi_ia(A, b, tol=1e-10, max_iter=100):

    N = len(b)

    x = np.zeros(N)
    xn = np.zeros(N)

    D = np.diag(A)
    R = A - np.diag(D)

    k = 0

    while norm(xn - x) > tol or k == 0:

        x = xn.copy()

        xn = (b - np.dot(R, x)) / D

        k += 1

        if k >= max_iter:
            print("No converge")
            break

    return xn

# RESOLUCIÓN DE SISTEMAS LINEALES POR GAUSS-SEIDEL --- GAUSS-SEIDEL CREEMOS QUE EL CÓSIGO ES VÁLIDO, PERO EL SISTEMA DIVERGE POR JACOBI Y SEIDEL

def my_gauss_seidel(A,b):
    N=len(b)
    x1,x2,R,U=zeros(N),zeros(N),zeros(N),zeros((N,N))
    U[:,:]=A[:,:]
    for i in range(N):
        U[i, :i+1]=0
    for i in range(N):
                    R[i]=b[i]-dot(A[i,i+1:],x1[i+1:])
    for i in range(N):
                    x2[i]=(R[i]-dot(A[i,:i],x2[:i]))/A[i,i]
    while norm(array(x2-x1))>=1e-16:
        x1=x2.copy()
        for i in range(N):
                             R[i]=b[i]-dot(A[i,i+1:],x1[i+1:])
        for i in range(N):
                             x2[i]=(R[i]-dot(A[i,:i],x2[:i]))/A[i,i]
    return x2


