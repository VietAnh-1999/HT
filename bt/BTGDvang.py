from datetime import datetime
import json
#khai bao class
class QLGD:
    def __init__(self):
        self.Ma_GD = ''
        self.ngayGD = ''
        self.dongia = 0
        self.soluong = 0
        self.loai = ''
#************************
    def nhapchungloai(self):
        self.Ma_GD = input("Nhap vao ma giao dich: ")
        while True:
            Ngay_nhap = input("Nhap vao ngay thang giao dịch(dd/mm/yy): ")
            try:
                self.ngayGD = datetime.strptime(Ngay_nhap,"%d/%m/%Y")
                break
            except ValueError:
                print("SAI DINH DANG, VUI LONG NHAL LAI ")
        
        while True:
            try:
                self.dongia = int(input("Nhap vao don gia:  "))
                break
            except:
                print("Nhap sai dinh dang!,Vui long nhap lai!")

        while True:
            try:
                self.soluong = int(input("Nhap vao so luong:  "))
                break
            except:
                print("Nhap sai dinh dang!,Vui long nhap lai!")

        while True:
            loai_GD = input("Nhap vao loại vang GD (18K,24k,9999): ")
            if loai_GD == "18K" or loai_GD == "24K" or loai_GD == "9999":
                self.loai = loai_GD
                break
            else:
                print("Nhap khong dung chung loai")

    def mua(self):
        print("Giao dich mua")
        total_price = self.soluong * self.dongia
#        print("{0} - {1} - {2} - {3} - {4} thanh tien = {5}".format(self.Ma_GD,self.ngayGD,self.loai,self.soluong,self.dongia,total_price))
        return(total_price)
    
    def  Ban(self):
        print("Giao dich ban")
        total_price = self.soluong * self.dongia *1.05
#        print("{0} - {1} - {2} - {3} - {4} thanh tien = {5}".format(self.Ma_GD,self.ngayGD,self.loai,self.soluong,self.dongia,total_price))
        return(total_price)
    
    def to_dict(self):
        return{
            "MaGiaoDich":self.Ma_GD,
            "NgayGiaoDich":str(self.ngayGD),
            "DonGia":self.dongia,
            "SoLuong":self.soluong,
            "Loai":self.loai,
            "Thanhtienmua":self.mua(),
            "Thanhtienban":self.Ban()
        }
             
#*******************************************************************************************************************************************************************
dict_data = []
QuanLy = QLGD()


key = input("Lua chon loai GD 1: Mua, 2: Ban: ")
if key == '1':
    QuanLy.nhapchungloai()
    dict_data.append(QuanLy.to_dict())
    print(dict_data)
    with open(r"D:\5.HT\HT\bt\QLGd.json", "w" , encoding = "utf-8") as f:
        json.dump(dict_data,f,indent=4)
