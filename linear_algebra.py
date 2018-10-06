import numpy as np

A=np.matrix([[1,1],[2,4]])
C=np.matrix([[35],[94]])


A_inv=np.linalg.inv(A)
B=A_inv*C
print(B)
