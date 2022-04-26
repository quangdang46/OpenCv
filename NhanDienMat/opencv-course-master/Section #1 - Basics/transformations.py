#pylint:disable=no-member

import cv2 as cv
import numpy as np

img = cv.imread("C:\\Users\\Admin\\OneDrive\\Code\\Python\\BAIHOC\\opencv-course-master\\Resources\\Photos\\park.jpg")
cv.imshow('Park', img)

# Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

# translated = translate(img, -100, 100)
# cv.imshow('Translated', translated)

# Rotation


'''
Hàm cv2.getRotationMatrix2D () được sử dụng để tạo ma trận biến đổi M sẽ được sử dụng để quay một hình ảnh.

Cú pháp: 

cv2.getRotationMatrix2D (tâm, góc, tỷ lệ)

Thông số: 

center: Tâm quay
angle (θ): Góc quay. Góc là dương cho ngược chiều kim đồng hồ và âm cho chiều kim đồng hồ.
scale: hệ số tỷ lệ chia tỷ lệ hình ảnh
'''
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]


    if rotPoint is None:
        rotPoint = (width//2,height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width,height)

    return cv.warpAffine(img, rotMat, dimensions)

# rotated = rotate(img, -45)
# cv.imshow('Rotated', rotated)
#
# rotated_rotated = rotate(img, -90)
# cv.imshow('Rotated Rotated', rotated_rotated)
#
# # Resizing
# resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
# cv.imshow('Resized', resized)
#
# # Flipping

'''
OpenCV-Python là một thư viện các chức năng lập trình chủ yếu nhắm vào thị giác máy tính thời gian thực. cv2.flip()được sử dụng để lật một mảng 2D. Hàm cv :: flip lật một mảng 2D quanh trục dọc, ngang hoặc cả hai.

Cú pháp: cv2.cv.flip (src, flipCode [, dst])

Các tham số:
src: mảng đầu vào.
dst: Mảng đầu ra có cùng kích thước và kiểu với src.
mã lật: Một cờ để chỉ định cách lật mảng; 0 có nghĩa là đảo quanh trục x và giá trị dương (ví dụ: 1) có nghĩa là đảo quanh trục y. Giá trị âm (ví dụ, -1) có nghĩa là đảo quanh cả hai trục.

Giá trị trả về: Nó trả về một hình ảnh.
'''
flip = cv.flip(img,1)
cv.imshow('Flip', flip)

# # Cropping
# cropped = img[200:400, 300:400]
# cv.imshow('Cropped', cropped)


cv.waitKey(0)