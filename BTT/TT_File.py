# #Tao file
# f = open("test1.txt","x")
import sqlite3
path = r"D:\5.HT\HT\BTT\test.db"
#path = r"D:\T\test.db"
connection = sqlite3.connect(path)
print(connection)
# tao doi tuong cursor
cursor = connection.cursor()
sql ="SELECT * FROM table1"
cursor.execute(sql)
t = cursor.fetchall()
# connection.close()
print(t)
#*********************************************
def print_item(t):
    for item in t:
        print(item)
print_item(t)
# for item in t:
#     if item[0]==1:
#         name = item[1]
#         diem = item[2]
#         print(name)
#         print(diem)
#     else:
#         print("khong ton tai")
found = False  # Biến kiểm tra đã tìm thấy chưa

for item in t:
    if item[0] == 15:  # thay bằng id bạn muốn tìm
        name = item[1]
        diem = item[2]
        print("Tên:", name)
        print("Điểm:", diem)
        found = True
        break

if not found:
    print("Không tồn tại")

bien1 = input("Nhap vao gia tri: ")
bien2 = input("Nhap vao gia tri: ")
# string = 'INSERT INTO table1(name) VAlUES ("' + bien1 + '")'
# sql = string
sql = "INSERT INTO table1(name,tuoi) VAlUES(?,?)"
cursor.execute(sql,(bien1,bien2,))
connection.commit()
sql = "DELETE FROM table1 WHERE stt = 13 or stt = 15"
cursor.execute(sql)
connection.commit()
print("ghjgfjhfgfgajdf")