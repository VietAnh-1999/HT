# # Khai bao class
# class SimpleClass:
#     #Attribute: khai bao bien
#     i = 0
#     #_init_ 
#     def __init__(self):
#         self.j = 7
#     # methods
#     def printMe(self):
#         print(self.j)

# objectA = SimpleClass()
# objectB = SimpleClass()

# objectA.printMe()
# print(objectB.i)



# tạo class
class Ngay:
    # thuoc tinh
    def __init__(self, Giatri_ngay,Giatri_thang,Giatri_nam):

        self.ngay = Giatri_ngay
        self.thang = Giatri_thang
        self.nam = Giatri_nam
    # Xac dinh so ngay cua thang
    @staticmethod
    def soNgayCuaThang(thang,nam):
        if (thang in [1,3,5,7,8,10,12]):
            return 31
        elif (thang in [4,6,9,11]):
            return 30
        elif (thang == 2):
            if(nam % 400 == 0 or (nam % 4 == 0 and nam % 100 !=0)):
                return 29
            else:
                return 28
            
    def ngaytrongnam(self):
        giaTriNgayTrongNam = 0
        #Tinh tong so luong ngay cua nhung thang truoc
        for x in range(1,self.thang):
            giaTriNgayTrongNam += self.soNgayCuaThang(x,self.nam)
        #Cong them so ngay hien tai
        giaTriNgayTrongNam += self.ngay
        return giaTriNgayTrongNam

#main
while True:
    x =  int(input("Nhap vao 1 de nhap vao ngay thang nam, nhao 0 de thoat:  "))
    if x==1:
        ngay_1 = int(input("Nhap vao ngay < 31: "))
        thang_1 = int(input("Nhap vao thang <12: "))
        nam_1 = int(input("Nhap vao nam:  "))
    elif x==0:
        break
    else:
        continue
    NgayA = Ngay(ngay_1,thang_1,nam_1)
    print("So ngay trong thang {} la: {}".format(thang_1,NgayA.soNgayCuaThang(thang_1,nam_1)))
    print("So ngay la: {}".format(NgayA.ngaytrongnam()))