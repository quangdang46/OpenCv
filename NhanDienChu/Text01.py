import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
img=cv2.imread("1.11.JPG")
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
boxes=pytesseract.image_to_data(img)
# print(enumerate(boxes.splitlines()))
# print(boxes)
# level	page_num	block_num	par_num	line_num	word_num	left	top	width	height	conf	text
for x,b in enumerate(boxes.splitlines()):
    if x!=0:
        b=b.split()
        #Co van ban do dai 12
        if len(b)==12:
            x,y,w,h=int(b[6]),int(b[7]),int(b[8]),int(b[9])
            # print(x)
            # print(b[11])

            #toa do x,y ,chieu rong ,chieu cao
            # print(x,t,h)


            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(img,b[11],(x,y),cv2.FONT_HERSHEY_TRIPLEX,2,(0,255,0),1)



cv2.imshow("Cua so",img)
cv2.waitKey()

cv2.destroyWindow()