import cv2
import hand as htm

cap=cv2.VideoCapture(0)
detector =htm.handDetector(detectionCon=0.55)
listpoin=[(0,0),(0,0)]
while True:
    rec,frame=cap.read()
    frame = detector.findHands(frame)
    lmList = detector.findPosition(frame, draw=False)
    # print(lmList)
    if len(lmList)!=0:
        listpoin.append((lmList[8][1],lmList[8][2]))

    cv2.imshow("Cuaso", frame)


    if cv2.waitKey(1)==ord("s"):
        break


cap.release()
cv2.destroyAllWindows()