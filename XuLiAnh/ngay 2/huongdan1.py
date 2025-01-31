# coding: utf-8
import imutils
import cv2


#Tải ảnh và hiển thị các thông số của ảnh
#Các ảnh là sự biểu thị của một mảng Numpy đa chiều với thông số
#số hàng (chiều cao) x số cột (chiều rộng) x số kênh (chiều sâu)
hinhanh = cv2.imread('du lieu mau/jp.png')
(h, w, d) = hinhanh.shape
print('Chiều rộng={}, chiều cao={}, số kênh={}'.format(w, h, d))

#Hiển thị ảnh trên màn hình
#Ấn phím bất kỳ để thoát màn hình xem trước
#cv2.imshow('Hình ảnh', hinhanh)
#cv2.waitKey(0)

#Truy cập vào pixel ở vị trí x=50, y=100
#Lưu ý rằng OpenCV lưu trữ hình ảnh BGR chứ k phải RGB
(B, G, R) = hinhanh[100, 50]
print('R={}, G={}, B={}'.format(R, G, B))

#Cắt một hình vuông ROI 100x100 từ ảnh đầu vào
#Bắt đầu từ vị trí x=320, y=60 và kết thúc tại x=420, y=160
roi = hinhanh[60:160, 320:420]
#cv2.imshow("ROI", roi)
#cv2.waitKey(0)

#Chỉnh cỡ hình ảnh về 200x200px, bỏ qua tỉ lệ
chinhco = cv2.resize(hinhanh, (200, 200))
#cv2.imshow('Chỉnh cỡ ảnh', chinhco)
#cv2.waitKey(0)

#Thay đổi kích thước cố định sẽ làm biến dạng khung hình
#Vì vậy hãy đổi kích thước về 300px và tính toán lại chiều rộng
#dựa vào tỉ lệ khung hình
tile = 300.0 / w
kichthuoc = (300, int(h * tile))
chinhco = cv2.resize(hinhanh, kichthuoc)
#cv2.imshow('Chinh co theo ti le', chinhco)
#cv2.waitKey(0)

#Một cách chỉnh cỡ khác mà không cần phải tính toán tỉ lệ
#là sử dụng thư viện imutils và truyền vào tham số width hoặc height
chinhco = imutils.resize(hinhanh, width=300)
#cv2.imshow('Chinh co bang imutils', chinhco)
#cv2.waitKey(0)

#Xoay ảnh 445 độ theo chiều kim đồng hồ bằng cách tính trung tâm của
#ảnh, sau đó xây dựng ma trận xoay và sau đó áp dụng nó
trungtam = (w // 2, h // 2)
matran = cv2.getRotationMatrix2D(trungtam, -45, 1.0)
xoayanh = cv2.warpAffine(hinhanh, matran, (w, h))
#cv2.imshow('Xoay anh', xoayanh)
#cv2.waitKey(0)

#Xoay ảnh bằng cách sử dụng thư viện imutils
xoayanh = imutils.rotate(hinhanh, -45)
#cv2.imshow('Xoay anh bang imutils', xoayanh)
#cv2.waitKey(0)

#Sau khi xoay ảnh, hình ảnh sẽ bịmất 1 vài phần do opencv không tự
#động chỉnh lại hình ảnh sau khi xoay
#Để hiển thị đầy đủ hình ảnh sau khi xoay thì sử dụng imutils
xoayanh = imutils.rotate_bound(hinhanh, 45)
#cv2.imshow('Xoay anh voi day du kich thuoc', xoayanh)
#cv2.waitKey(0)

#Làm mịn ảnh bằng phương pháp làm mờ Gaussian với một nhân 11x11
#hữu dụng khi cần giảm nhiễu tần số cao
lammo = cv2.GaussianBlur(hinhanh, (11, 11), 0)
#cv2.imshow('Lam mo anh', lammo)
#cv2.waitKey(0)

#Vẽ một hình vuông đỏ với độ dày đường viền là 2px xung quanh mặt
ketqua = hinhanh.copy()
cv2.rectangle(
        ketqua, #Ảnh kết quả
        (320, 60), #Tọa độ điểm bắt đầu trên cùng bên trái
        (420, 160), #Tọa độ điểm kết thúc dưới cùng bên phải
        (0, 0, 255), #Mã màu ở dạng BGR
        2, #Độ dày đường viền
        )
#cv2.imshow('Ve hinh vuong', ketqua)
#cv2.waitKey(0)

#Vẽ một hình tròn màu xanh có đường kính 20px, tọa độ tâm là
#x=300, y=150
ketqua = hinhanh.copy()
cv2.circle(
        ketqua,
        (300, 150), #Tọa độ tâm
        20, #Đường kính
        (255, 0, 0), #Mã màu theo hệ BGR
        -1, #Độ dày đường viền, -1 tức là đổ màu toàn bộ hình
        )
#cv2.imshow('Ve hinh tron', ketqua)
#cv2.waitKey(0)

#Vẽ đường thẳng đỏ dày 5px từ x=60,y=20 đến x=400,y=200
ketqua = hinhanh.copy()
cv2.line(
        ketqua, #Ảnh kết quả
        (60, 20), #Tọa độ điểm bắt đầu
        (400, 200), #Tọa độ điểm kết thúc
        (0, 0, 255), #Mã màu dạng BGR
        5, #Độ dày đường kẻ
        )
#cv2.imshow('Ve duong thang', ketqua)
#cv2.waitKey(0)

#Vẽ dòng chữ xanh lên hình ảnh
ketqua = hinhanh.copy()
cv2.putText(
        ketqua, #Ảnh kết quả
        "Học OpenCV trên Python 3", #Nội dung văn bản
        (10, 25), #Vị trí bắt đầu của văn bản
        cv2.FONT_HERSHEY_SIMPLEX, #Font chữ cho văn bản
        0.7, #Cỡ chữ
        (0, 255, 0), #Màu chữ
        2, #Độ dày của chữ
        )
cv2.imshow('Viet chu', ketqua)
cv2.waitKey(0)
