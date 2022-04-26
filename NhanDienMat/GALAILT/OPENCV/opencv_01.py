import cv2
#Doc anh
import imutils

img=cv2.imread("2.PNG",1)
# #Xuat anh mac dinh
# cv2.imshow("Hien thu",img)

#Xuat anh theo kich thuoc
# hk=cv2.resize(img,(200,400))
hk=cv2.resize(img,(0,0),fx=0.5,fy=0.5)
#Xoay anh
# hk=cv2.rotate(hk,cv2.ROTATE_180)
# cv2.imshow("Cua so",hk)


##################################
#Xoay anh su dung thu vien imutils
image=imutils.rotate(img,90)
cv2.imshow("Xoay anh",image)
##################################

#Thoi gian doi ms
#Tao phim luu anh
k=cv2.waitKey()
if k==ord("s"):
    cv2.imwrite("anhmoi.jpg",img)
