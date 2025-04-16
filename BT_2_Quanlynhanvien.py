#Khai bao class 
#Branch Json

import json
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
                if any(nv.get_ma_nhan_vien () == ma for nv in danh_sach_nv ):
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
     
        
    def printInfo(self):
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
    # tra ve dang dict  de chuyen sang json
    def to_dict(self):
        return{
            "ma_nhan_vien": self.__ma_nhan_vien,
            "ten":self.ten,
            "tuoi":self.tuoi,
            "dia_chi":self.dia_chi,
            "luong":self.luong,
            "gio_lam":self.gio_lam,
            
        }
# doc data theo dinh dang json
    @staticmethod
    def from_dict(data):
            nv = NhanVien()
            nv.__ma_nhan_vien = data["ma_nhan_vien"]
            nv.ten = data["ten"]
            nv.tuoi = data["tuoi"]
            nv.dia_chi = data["dia_chi"]
            nv.luong = data["luong"]
            nv.gio_lam =data["gio_lam"]
            return nv

#main***********************************************************************************************************************************
danh_sach_nv = []
NhapNhanVien = NhanVien()
#Doc du lieu tu file
def doc_Json():
    try:
        with open("nhanvien.json","r", encoding= "utf-8") as f:
            data = json.load(f)
            print(data)
        print("da doc danh sach tu file json")
        return data
    except FileNotFoundError:
        print("File khong ton tai")
    except json.JSONDecodeError:
        print("File JSON bi loi hoac rong")


#Tuy xuat thong tin nhan vien
# def truyxuatthongtin_NV():
#     print("nhap '-1' de thoat")
#     print("*"*60)
#     while True:
#         ma_nv = input("Nhap vao ma nhan vien can truy xuat: ")
#         if any(nv.get_ma_nhan_vien () == ma_nv for nv in danh_sach_nv ):
#             for nv in danh_sach_nv:
#                 if nv.get_ma_nhan_vien() == ma_nv:
#                     nv.printInfo()
#                     print("*"*60)
#         elif ma_nv == '-1':
#             break
#         else:
#             print("Ma khong ton tai!")


data=doc_Json()
while True:
    i = input("Nhap vao 'In' de nhap thong tin nhan vien\nNhap vao 'Exit' de thoat ")
    if i == "In":
        NhapNhanVien = NhanVien()
        NhapNhanVien.inputInfo(danh_sach_nv)
        NhapNhanVien.printInfo()
        # Viet du lieu vao file txt
        data.append(NhapNhanVien.to_dict())

        with open("nhanvien.json", "w", encoding="utf-8") as f:
            json.dump(data,f,indent=4)
            print("Da gui du lieu vao file thanh cong")

    elif i == "Exit":
        break
    doc_Json()
    # elif i== 'A':
    #     truyxuatthongtin_NV()
        

