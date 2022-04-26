import cv2
import numpy as np
cap=cv2.VideoCapture(0)
while True:
    #ret tra ve true false
    ret,frame=cap.read()
    # print(ret)
    width=int(cap.get(3))#Lay chieu rong
    hight=int(cap.get(4))#Lay chieu cao
    small_frame=cv2.resize(frame,(0,0),fx=0.5,fy=0.5)
    image=np.zeros(frame.shape,np.uint8)
    image[:hight//2,:width//2]=small_frame
    image[hight // 2:, :width // 2] = cv2.rotate(small_frame,cv2.ROTATE_180)
    image[hight // 2:, width // 2:] = small_frame
    image[:hight // 2, width // 2:] = small_frame
    #uint8 kieu so nguyen 8 bit


    # cv2.imshow("Cua So",frame)
    cv2.imshow("Cua So",image)

    #chu y dat thoi gian delay
    if cv2.waitKey(1)==ord("s"):
        break
#giai phong cam
cap.release()
#tat het tat ca cua so
cv2.destroyAllWindows()