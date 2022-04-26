import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

def DocAnh(path,listpic):
    listTmp=[]
    for img in listpic:
        curImg=cv2.imread(f"{path}/{img}")
        listTmp.append(curImg)
    print("Done!!Pic")
    return listTmp

def DocQuanBai(path,listpic):
    listName=[]
    for img in listpic:
        curImg=cv2.imread(f"{path}/{img}")
        listName.append(os.path.splitext(img)[0])
    print("Done!!Name")
    return listName

def Encodepic(images):
    EndCodeList=[]
    # print(images)
    for img in images:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode=face_recognition.face_encodings(img)
        EndCodeList.append(encode)
    print("Ma hoa thanh cong!!")
    return EndCodeList



listSo = os.listdir("SoBai")
listQuan = os.listdir("QuanBai")
####################################
listSoBai=DocAnh("SoBai",listSo)#Chua ma tran anh so
listNameBai=DocQuanBai("SoBai",listSo)#chua list name so
listQuanBai=DocAnh("QuanBai",listQuan)#chua ma tran anh so quan bai
listNameQuan=DocQuanBai("QuanBai",listQuan)#chua list name quan bai
###################################
EncodeSo=Encodepic(listSoBai)
EncodeQuan=Encodepic(listQuanBai)

# print(listSoBai)

cap=cv2.VideoCapture(0)
while True:
    rec,frame=cap.read()
    # frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    # faceFrame=face_recognition.face_locations(frame)
    # faceEncode=face_recognition.face_encodings(frame)
    # # print(faceFrame)
    #
    # for encodeFace,FaceLoc in zip(faceEncode,faceFrame):
    #     try:
    #         y1,x2,y2,x1=FaceLoc
    #         cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),1)
    #         print("resss")
    #     except:
    #         pass

    cv2.imshow("Cua So",frame)

    if cv2.waitKey(1)==ord("s"):
        break
cap.release()
cv2.destroyAllWindows()
