# List = ["Anh","Chi","Em"]
# number = [1,4,3,5,6,5,5,5,5,5,5,5,2,7,123,45,65,776,75,34]
# # print(List)

# # List.append("Viet")
# # print(List)

# # List.insert(1,"The")
# # print(List)
# # print(List.count("Viet"))

# List.sort()
# print(List)
# number.sort()
# print(number)
# number.sort(reverse=True)
# print(number)
# print(number.count(5))
# x = int(input("Nhap vao so nguyen x: "))
# print(" bang cuu chương {0} toi 10 la: ".format(x))
# for i in range(x,11):
#     print("bang cuu chuong {}".format(i))
#     for j in range(1,11):
#         print("{0} x {1} = {2}".format(i,j,i*j))
# print("Ket thuc chuong trinh")


chuoi = str(input("Nhap vao mot chuoi: "))
while True:
    x = int (input("Nhap vao lua chon X: "))
    if x==1:
        chuoi = chuoi.upper()
        print(chuoi)
    elif x==2:
        chuoi  = str.capitalize(chuoi)
        print(chuoi)
    elif x == 3:
        chuoi = chuoi.lower()
        print(chuoi)
    elif x== 4:
        list_1 = chuoi.split(" ")
        print(list_1)
    elif x==5 :
        print("dung chuong trinh")
        break
    else:
        x = int (input("Nhap vao lua chon X: "))