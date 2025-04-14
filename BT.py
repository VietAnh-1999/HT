print("toll giải phương trình ax^2 + bx + c = 0")
a = float(input("Nhap a: "))
while a == 0:
    print("Không được nhập a = 0")
    a = float(input("Nhap a khác 0 : "))
# abc

b = float(input("Nhap b: "))
c = float(input("Nhap c: "))

if (a != 0):
    delta = b**2 - 4*a*c
    if (delta < 0):
        print("Phuong trinh vo nghiem")
    elif (delta == 0):
        x1 = x2 = (-b/2*a)
        print("Phuong trinh co nghiem kep x1=x2= ",x1)
    else:
        x1 = (-b + delta**0.5)/2*a
        x2 = (-b - delta**0.5)/2*a
        print("Phuong trinh co 2 nghiem: ", end = ", "); print("X1=",x1, end = ", "); print("x2=",x2)