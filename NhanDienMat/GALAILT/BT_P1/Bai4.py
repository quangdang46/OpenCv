import numpy as np
# z=np.array([[34,43,73],[82,22,12],[53,94,66]])
# A=z[:,0].copy()
# z[:,0]=z[:,2].copy()
# z[:,2]=A.copy()
# print(z)
z=np.array([[34,43,73],[82,22,12],[53,94,66]])

B=z[0,:].copy()
z[0,:]=z[1,:].copy()
z[1,:]=B.copy()
print(z)