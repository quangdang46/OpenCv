import numpy as np
z=np.array([[34,43,73],[82,22,12],[53,94,66]])

print(z)

MAX=max(list(z[0]))
for i in range(z.shape[0]):
    if MAX>max(list(z[i])):
        MAX=max(list(z[i]))



MIN=min(list(z[0]))
for i in range(z.shape[0]):
    if MIN<min(list(z[i])):
            MIN=min(list(z[i]))

