import cv2
import os # luu anh vao path 
# Đường dẫn folder
path = r"D:\5.HT\anh\anh1.png"
# Load the image 1 là có màu 0 là không màu (theo đường dẫn)
#image = cv2.imread(path,1)
# load ảnh ở trong thư mục
image = cv2.imread("anh.png",1)
# duong dan luu anh
path1 = r"D:\5.HT\anh"
os.chdir(path1)
# Display the image
cv2.imshow("Image", image)
# lưu anh vừa hiển thị 

filename = "anhmoi1.jpg"
cv2.imwrite(filename,image)
# thời gian hiện ảnh ms
cv2.waitKey(1000)

# Close all windows
cv2.destroyAllWindows()