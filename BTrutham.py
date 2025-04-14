# Bai tap rut tham trung thuong
# import ramdom
import random
Thung = set()
#////
while True:
    print("---------------Menu---------------")
    print("1-  Them ma du thuong")
    print("2-  Xoa ma du thuong")
    print('3-  Quay so ngau nhien')
    print('4-  Ket thuc chuong trinh')
    print("Thung phieu hien tai la: ")
    print(Thung)

    while True:
        luaChon = input('Hay nhap vao lua chon cua ban: ')
        if luaChon.isdigit():
            luaChon = int(luaChon)
            break
        print("Vui long nhap lai lua chon hop le")
            
    if  luaChon == 1:
        print("*****************Tao Ma************************")
        while True:
            maduthuong = input('Hay nhap vao mot ma du thuong:  ')
            if maduthuong == '0':
                break
            if maduthuong in Thung:
                print("ma du thuong da ton tai", end=","); print("Vui long nhap lai ma du thuong")
            else:
                Thung.add(maduthuong)
    elif luaChon == 2:
        print("*****************Xoa Ma************************")
        macanxoa = input("Hay nhap vao ma du thuong can xoa: ")
        Thung.discard(macanxoa)
    elif luaChon == 3:
        print("*****************Nguoi Trung Thuong************************")
        i = random.randint(0,len(Thung))
        j = 0
        for x in Thung:
            if i == j:
                break
            j +=1
        print("Chu mung nguoi co ma '{0}'da trung thuong".format(x))
        Thung.discard(x)

    elif luaChon == 4:
        print("******* Dung Chuong Trinh Quay Thuong *********")
        break
    D = input("Nhan mot nut bat ki de tiep tuc")  


