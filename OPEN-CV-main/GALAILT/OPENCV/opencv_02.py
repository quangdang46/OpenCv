import cv2
from random import randint
img=cv2.imread("2.PNG",1)
# print(type(img))
# print(img.shape)
#Tao mot hang bat ki

# for i in range(100):
#     for j in range(img.shape[1]):
#         img[i][j]=[randint(0,255),randint(0,255),randint(0,255)]
#Copy vung anh

vungchon=img[0:100,400:700]
#Luu y phai cung kich thuoc
img[100:200,500:800]=vungchon
# cv2.imwrite("Test.jpg",vungchon)
cv2.imshow("Hien thi",img)
k=cv2.waitKey()