#Khai bao class 
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
    
    @staticmethod
    def from_string(data_str):
        part = data_str.strip().split(",")
        if len(part)>= 6:
            nv = NhanVien()
            nv.__ma_nhan_vien = part[0]
            nv.ten =part[1]
            nv.tuoi =int(part[2])
            nv.dia_chi = part[3]
            nv.luong = float(part[4])
            nv.gio_lam = float(part[5])
            return nv
        else:
            return None

#main***********************************************************************************************************************************
danh_sach_nv = []
NhapNhanVien = NhanVien()
#Doc du lieu tu file
def xuatdulieura_TXT():
    try:
        with open("nhanvien.txt","r", encoding= "utf-8") as f:
            for line in f:
                nv =  NhanVien.from_string(line)
                if nv is not None:
                    danh_sach_nv.append(nv)
        print("da doc danh sach tu file")
    except FileNotFoundError:
        print("File khong ton tai")
#Tuy xuat thong tin nhan vien
def truyxuatthongtin_NV():
    print("nhap '-1' de thoat")
    while True:
        print("*"*60)
        ma_nv = input("Nhap vao ma nhan vien can truy xuat: ")
        if any(nv.get_ma_nhan_vien () == ma_nv for nv in danh_sach_nv ):
            for nv in danh_sach_nv:
                if nv.get_ma_nhan_vien() == ma_nv:
                    nv.printInfo()
                    print("*"*60)
        elif ma_nv == '-1':
            break
        else:
            print("Ma khong ton tai!")

xuatdulieura_TXT()
# In danh sach
if danh_sach_nv:
    print("== Danh sách nhân viên đã đọc từ file ==")
    for nv in danh_sach_nv:
        nv.printInfo()
        print("-" * 40)


while True:
    i = input("Nhap vao 'In' de nhap thong tin nhan vien\nNhap vao 'Exit' de thoat ")
    if i == "In":
        NhapNhanVien = NhanVien()
        NhapNhanVien.inputInfo(danh_sach_nv)
        NhapNhanVien.printInfo()
        # Viet du lieu vao file txt
        with open("nhanvien.txt", "a", encoding="utf-8") as f:
            f.write(NhapNhanVien.to_string() + "\n")
            print("Da gui du lieu vao file thanh cong")
        xuatdulieura_TXT()
    elif i == "Exit":
        break
    elif i== 'A':
        truyxuatthongtin_NV()
        

# with open("ds.json", 'r', encoding='utf-8') as f:
#     data = json.load(f)

# print(data[0]["manv"])

# with open("nhanvien.json", "a", encoding="utf-8") as f:
#         # f.write(sdata)
#         sdata=json.dump(data,f, ensure_ascii=False, indent=4)