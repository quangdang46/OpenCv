import cv2
import face_recognition
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()

    try:
        capLoc=face_recognition.face_locations(frame)[0]
        # print(type(capLoc[0]))
        y1,x2,y2,x1=capLoc[0],capLoc[1],capLoc[2],capLoc[3]
        cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),-11)

    except:
        print("Error!!")


    cv2.imshow("CuaSo",frame)


    if cv2.waitKey(1)==ord("s"):
        break

cap.release()
cv2.destroyAllWindows()