#coding: utf-8
import argparse
import imutils
import cv2


#Xây dựng các tham số và lấy các tham số
tuychon = argparse.ArgumentParser()
tuychon.add_argument(
        '-i',
        '--image',
        required=True,
        help='Đường dẫn tệp ảnh',
        )
cactuychon = vars(tuychon.parse_args())

#Tải ảnh đầu vào từ tham số đường dẫn ảnh và hiển thị nó ra màn hình
hinhanh = cv2.imread(cactuychon['image'])
#cv2.imshow('Hinh anh', hinhanh)
#cv2.waitKey(0)

#Chuyển ảnh sang dạng đen trắng
dentrang = cv2.cvtColor(
        hinhanh,
        cv2.COLOR_BGR2GRAY,
        )
#cv2.imshow('Anh den trang', dentrang)
#cv2.waitKey(0)

#Sử dụng trình phát hiện cạnh để tìm đường viền ngoài của các đối tượng trong
#hình ảnh
timcanh = cv2.Canny(
        dentrang, #Ảnh đen trắng
        30, #Giá trị điểm ảnh nhỏ nhất
        150, #Giá trị điểm ảnh lớn nhất
        )
#cv2.imshow('Tim kiem canh', timcanh)
#cv2.waitKey(0)

#Đặt ngưỡng hình ảnh bằng cách đặt tất cả các giá trị điểm ảnh nhỏ hơn 225
#(màu trắng, hình nổi) và tất cả giá trị điểm ảnh từ trên 225 đến 255 (màu đen,
#hình nền), từ đó phân chia các hình ảnh
chianguong = cv2.threshold(
        dentrang, #Ảnh đen trắng
        225, #Ngưỡng nhỏ nhất
        255, #Ngưỡng lớn nhất
        cv2.THRESH_BINARY_INV,
        )[1]
#cv2.imshow('Chia nguong', chianguong)
#cv2.waitKey(0)

#Tìm các đường viền của các đối tượng nổi trên ảnh đã chia ngưỡng
cacduongvien = cv2.findContours(
        chianguong.copy(), #Sao chép ảnh chia ngưỡng ra làm ảnh đầu vào
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE, #Các tham số này sẽ tìm hiểu sau
        )
cacduongvien = imutils.grab_contours(cacduongvien)
ketqua = hinhanh.copy()

#Lặp qua các đường viền tìm được
for duongvien in cacduongvien:
    #Mỗi đường viền trên ảnh kết quả vẽ một đường kẻ tím 3px sau đó hiển thị
    #các đường viền đó
    cv2.drawContours(
            ketqua,
            [duongvien],
            -1,
            (240, 0, 159),
            3,
            )
#cv2.imshow('Ve cac duong vien', ketqua)
#cv2.waitKey(0)

#Hiển thị thông báo tìm thấy các đối tượng trên ảnh
noidung = 'Tim thay {} doi tuong'.format(len(cacduongvien))
cv2.putText(
        ketqua,
        noidung,
        (10, 25),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (240, 0, 159),
        2)
#cv2.imshow('Ve duong vien', ketqua)
#cv2.waitKey(0)

#Giảm kích thước của các đối tượng nổi
matna = chianguong.copy()
matna = cv2.erode(
        matna,
        None,
        iterations=5, #Số lần lặp
        )
#cv2.imshow('Giam kich thuoc doi tuong', matna)
#cv2.waitKey(0)

#Tăng kích thước của các đối tượng nổi
matna = chianguong.copy()
matna = cv2.dilate(
        matna,
        None,
        iterations=5,
        )
#cv2.imshow('Tang kich thuoc', matna)
#cv2.waitKey(0)

#Sử dụng mặt nạ để cắt các đối tượng nổi sử dụng toán tử AND để kết hợp ảnh đầu
#vào với ảnh mặt nạ
matna = chianguong.copy()
ketqua = cv2.bitwise_and(
        hinhanh, #Ảnh đầu vào
        hinhanh,
        mask=matna,
        )
#cv2.imshow('Ket qua cat anh', ketqua)
#cv2.waitKey(0)
