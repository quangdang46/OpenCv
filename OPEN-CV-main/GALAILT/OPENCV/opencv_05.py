import cv2
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    width=int(cap.get(3))
    height=int(cap.get(4))
    #Ve duong
    # img=cv2.line(frame,(0,0),(width,height),(0,0,0),50)
    # img=cv2.line(frame,(0,height),(width,0),(255,255,255),50)
    '''
    #(0, 0) điểm bắt đầu vẽ line
    #(width,height) điểm kết thúc
    # (0,0,0) mã màu RGB
    # 50 : độ dày đường line
    '''
    #Ve hinh chu nhat
    # img=cv2.rectangle(frame,(100,100),(200,400),(230,124,0),10)
    #Neu do day =-1 thi se phu kin hinh chu nhat


    #Ve hinh tron
    # img=cv2.circle(frame,(100,100),70,(0,124,24),5)
    #70 la duong kinh

    #Chen van ban

    font=cv2.FONT_HERSHEY_PLAIN
    img=cv2.putText(frame,"Xin chao",(0,100),font,3,5)




    cv2.imshow("Cua so",frame)

    if cv2.waitKey(1)==ord("s"):
        break

cap.release()
cv2.destroyAllWindows()
