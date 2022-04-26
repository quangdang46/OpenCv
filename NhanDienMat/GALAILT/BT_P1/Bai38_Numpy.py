import numpy as np
from random import randint
z=[]
for i in range(20):
    z.append(randint(1,20))
z=np.array(z).reshape(4,5)
# z=np.arange(20).reshape(5,4)
# print(z)

# #Kiem tra so chieu cua mang
# print("So chieu cua mang ",z.ndim)
# print('So luong phan tu ',z.size)
# print("Kich thuoc mang ",z.shape)
# #Sap xep mang
# z=np.sort(z)
# print(z)


#tao mang cac phan tu cach deu nhau
# z=np.linspace(1,10,5)
# print(z)

#tao mang toan so 1
# z=np.ones((3,5,))
# print(z)

# #tao mang toan so 0
# z=np.zeros((3,5))
# print(z)

# Lay phan tu
# print(z[0,1])
# print(z[0][1])

#Lay dong
# print(z[1,:])
# #Lay cot
# print("*"*10)
# print(z[:,2])


#Thay doi gia tri
# print(z)
# z[0,1]=100
# # z[1:3,1:3]=[9999,10000]
# z[1:3,1]=[9999,10000]
# print(z)


#Kiem tra phan tu co ton tai hay khong
# print(z)
# print(2 in z)
# print(666 in z)


#Tim vi tri 1 phan tu trong mang
print(z)
n=int(input())
for i in range(z.shape[0]):
    for j in range(z.shape[1]):
        if z[i,j]==n:
            print((i,j))