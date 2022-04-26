#pylint:disable=no-member

import cv2 as cv

# Read in an image
img = cv.imread("C:\\Users\\Admin\\OneDrive\\Code\\Python\\BAIHOC\\opencv-course-master\\Resources\\Photos\\park.jpg")
cv.imshow("Park",img)

# # Converting to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# # Blur
#Lam mo anh
# blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

# # Edge Cascade
# #Lay canh cua anh
# canny = cv.Canny(img, 125, 175)
# cv.imshow('Canny Edges', canny)

# # Dilating the image
# #Tang dien tich tiep xuc anh
# dilated = cv.dilate(img, (7,7), iterations=3)
# cv.imshow('Dilated', dilated)

# # Eroding
# # Xoi mon hinh anh
# eroded = cv.erode(img, (7,7), iterations=3)
# cv.imshow('Eroded', eroded)

# # Resize
# # Thay doi kich thuoc anh
# resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
# cv.imshow('Resized', resized)
#
# # Cropping
# # Copy anh
# cropped = img[50:200, 200:400]
# cv.imshow('Cropped', cropped)

cv.waitKey()