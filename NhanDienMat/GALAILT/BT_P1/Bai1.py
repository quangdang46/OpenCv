#EX1
1#
import numpy as np
z=np.zeros((5,5))
z[0,:]=1
z[4,:]=1
z[:,0]=1
z[:,4]=1
print(z)
2#
z=np.ones((5,5))
z[0,:]=0
z[4,:]=0
z[:,0]=0
z[:,4]=0
print(z)