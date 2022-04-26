#pylint:disable=no-member

import cv2 as cv
import numpy as np

img = cv.imread("C:\\Users\\Admin\\OneDrive\\Code\\Python\\BAIHOC\\opencv-course-master\\Resources\\Photos\\cats.jpg")
cv.imshow('Cats', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

canny = cv.Canny(blur, 125, 175)
#125 175 la gia tri nguong
cv.imshow('Canny Edges', canny)

# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.imshow('Thresh', thresh)


#Tim duong vien
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
#contours tra ve toa do cac duong bao
print(f'{len(contours)} contour(s) found!')
# print(contours)


cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)