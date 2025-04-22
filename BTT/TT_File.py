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