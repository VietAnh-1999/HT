#Khai bao class 
#  day la main
class NhanVien:

    def __init__(self):
        self.__ma_nhan_vien = ""
        self.ten = ''
        self.tuoi = 0
        self.dia_chi = ''
        self.luong = 0
        self.gio_lam = 0
    # Lay du lieu name mangling ( kieu du lieu co dau gach duoi) nhu kieu key trong lop
    def get_ma_nhan_vien(self):
        return self.__ma_nhan_vien

    # phuong thuc
    def inputInfo(self,danh_sach_nv):
            while True:
                ma = input("Nhap vao ma nhan vien:  ")
                if ma in danh_sach_nv:
                    print("Max nhan vien da ton tai! Vui long nhap lai ma nhan vien khac")
                else:
                    self.__ma_nhan_vien = ma
                    break
       
            self.ten = input("Nhap vao ten nhan vien co ma nhan vien {}: ".format(self.__ma_nhan_vien))
            while True:
                try:
                    self.tuoi = int(input("Nhap vao tuoi nhan vien co ma nhan vien {}: ".format(self.__ma_nhan_vien)))
                    break
                except:
                    print("Ban phai nhap tuoi la so nguyen")
            self.dia_chi = input("Nhap vao dia chi cua nhan vien co ma nhan vien {}: ".format(self.__ma_nhan_vien))
            while True:
                try:
                    self.luong = float(input("Nhap vao luong cua nhan vien co ma nhan vien {}: ".format(self.__ma_nhan_vien)))
                    break
                except:
                    print("Ban phai nhap luong la 1 so")
            while True:
                try:
                    self.gio_lam = float(input("Nhap vao gio lam cua nhan vien co ma nhan vien {}: ".format(self.__ma_nhan_vien)))
                    break
                except:
                    print("Ban phai nhap gio lam la mot so")
     
        
    def printInfo(self,manhanvien):
        print("Mã nhân viên:", self.__ma_nhan_vien)
        print("Tên:", self.ten)
        print("Tuổi:", self.tuoi)
        print("Địa chỉ:", self.dia_chi)
        print("Lương:", self.luong)
        print("Giờ làm:", self.gio_lam)
        print("Thưởng:", self.tinhThuong())

    def tinhThuong(self):
        if self.gio_lam >= 200:
            return self.luong * 0.2
        elif self.gio_lam >= 100:
            return self.luong * 0.1
        else:
            return 0
    # tra ve chuoi
    def to_string(self):
        return f"{self.__ma_nhan_vien},{self.ten},{self.tuoi},{self.dia_chi},{self.luong},{self.gio_lam},{self.tinhThuong()}"

#main***********************************************************************************************************************************
danh_sach_nv = []

while True:
    i = input("Nhap vao 'In' de nhap thong tin nhan vien\nNhap vao 'Exit' de thoat ")
    if i == "In":
        NhapNhanVien = NhanVien()
        NhapNhanVien.inputInfo(danh_sach_nv)
        danh_sach_nv.append(NhapNhanVien)

        NhapNhanVien.printInfo(NhapNhanVien.get_ma_nhan_vien())
        # Viet du lieu vao file txt
        with open("nhanvien.txt", "a", encoding="utf-8") as f:
            f.write(NhapNhanVien.to_string() + "\n")
            print("Da gui du lieu vao file thanh cong")

    elif i == "Exit":
        break