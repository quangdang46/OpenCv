import cv2
import time
import os
import hand as htm
pTime=0
cap=cv2.VideoCapture(0)

FolderPath="Fingers"
lst=os.listdir(FolderPath)
lst_2=[]
for i in lst:
    img=cv2.imread(f"{FolderPath}/{i}",1)
    lst_2.append(img)
# print(lst)
detector=htm.handDetector(detectionCon=0.55)
fingerid=[4,8,12,16,20]
while True:
    ret,frame=cap.read()
    fram=detector.findHands(frame)
    lmlist=detector.findPosition(frame,draw=False)#phat hien vi tri day 20 diem vao list
    cv2.rectangle(frame,(0,200),(150,400),(0,255,0),-1)
    if len(lmlist)!=0:
        fingers=[]
        # print(fingers)
        # Viet ngon cai diem uon nam ben trai hay ben phai 3
        if lmlist[fingerid[0]][1] > lmlist[fingerid[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        # print(fingers)

        for id in range(1,5):
            # Viet ngon dai
            if lmlist[fingerid[id]][2]<lmlist[fingerid[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        soluong=fingers.count(1)
        # print(soluong)

        h,w,c=lst_2[soluong-1].shape
        frame[0:h,0:w]=lst_2[soluong-1]
        cv2.putText(frame, f"{soluong}", (50,320), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 12)


    #Tim FPS
    cTime=time.time()
    fps=1/(cTime-pTime)
    # print(fps)
    pTime=cTime
    #hien thi FPS
    font=cv2.FONT_HERSHEY_DUPLEX
    cv2.putText(frame,f"FPS:{int(fps)}",(200,50),font,2,(255,0,0),1)
    cv2.imshow("Cua so",frame)

    if cv2.waitKey(1)==ord("s"):
        break

cap.release()
cv2.destroyAllWindows()