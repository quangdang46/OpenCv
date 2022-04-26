import numpy as np
z=np.zeros((8,8))
for i in range(z.shape[0]-1):
    if i%2==1:
        z[0:7,i]=1
    else:
        z[7,i]=1
print(z)