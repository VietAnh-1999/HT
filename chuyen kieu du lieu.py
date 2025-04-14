x =  int(input("Nhap vao so  can chuyen:  "))
y =  int(input("Nhap vao he co so du lieu: "))
kq =""
while (x > 0):
    kq = str(x % y) + kq
    x = x // y
print(kq)
