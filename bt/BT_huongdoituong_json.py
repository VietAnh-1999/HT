# main
# Student
#Khai bao Class
import json
class Student:
    def __init__(self):
        _id = ''
        ten = ''
        diem_trung_binh = 0.0
        tuoi = 0
        lop = ""

    def get_id(self):
        return self._id

#
    def inputInfo(self):
        
        while True:
            id_student = input("Nhap vao 'id' cho hoc sinh: ")
            if len(id_student) >= 8:
                self._id = id_student
                break
            else:
                print("Phai nhap id dai hon 8 ky tu!")

        self.ten = input("Nhap vao ten cho sinh vien co 'id':{}: ".format(self._id))

        while True:
            diem_tb = int(input('Nhap vao diem trung binh cho sinh vien co "id": {} : '.format(self._id) ))
            if 0.0 <= diem_tb <= 10 :
                self.diem_trung_binh = diem_tb
                break
            else:
                print("vui long nhap diem cho hoc sinh tu 0.0 --->10 !")
        while True:
            try:
                tuoi = int(input('Nhap vao tuoi cua sinh vien co "id": {} : '.format(self._id) ))
                if tuoi >= 18:
                    self.tuoi = tuoi
                    break
                else:
                    print("vui long nhap tuoi cho hoc sinh lon hon 18!")
            except:
                print("Khong dung dinh dang ! Phai nhap so nguyen")
        while True:
            lop = input("nhap vao ten lop cho hoc sinh\n(Ten lop bat dau bang 'A' hoac 'C'): ")
            if lop[0] == 'A' or lop[0] == 'C':
                self.lop = lop
                break
            else:
                print("Sai dinh dang vui long nhap lai!")
    def showInfo(self):
        print("Ten hoc sinh: {}".format(self.ten))
        print("Ma ID cua hoc sinh {} la: {}".format(self.ten,self._id))
        print("Diem cua hoc sinh {} la: {}".format(self.ten,self.diem_trung_binh))
        print("Tuoi cua hoc sinh {} la: {}".format(self.ten,self.tuoi))
        print("Lop cua hoc sinh {} la: {}".format(self.ten,self.lop))
        print(self.Xet_hb())


    def Xet_hb(self):
        if self.diem_trung_binh > 8.0:
            return "Hoc sinh gioi 'Duoc Hoc Bong'"
        else:
            return "Khong Duoc Hoc Bong"
    
    # chuyen sang kieu tu dien
    def to_dict(self):
        return{
            "id":self._id,
            "name":self.ten,
            "score":self.diem_trung_binh,
            "age":self.tuoi,
            "class":self.lop
        }
    # chuyển tu object sang dict
    @staticmethod
    def from_dict(Json_data):
        nv = Student()
        nv._id = Json_data["id"]
        nv.ten = Json_data["name"]
        nv.diem_trung_binh = Json_data["score"]
        nv.tuoi = Json_data["age"]
        nv.lop = Json_data["class"]
        return nv
# main *************************************************************************************************************************************************************************
Hocsinh = Student()
#doc data tu file Json
def read_data():
    try:
        with open("dulieuhs.json","r",encoding= "utf-8") as f:
            data = json.load(f)
            return data        
    except FileNotFoundError:
        print("File khong ton tai")
    except json.JSONDecodeError:
        print("File json rong hoac khong ton tai")
    
#input data vao file Json
def input_data():
    Hocsinh.inputInfo()
    Hocsinh.showInfo()
    data.append(Hocsinh.to_dict())
    with open("dulieuhs.json","w",encoding= "utf-8") as f:
        json.dump(data,f,indent=4)
        print("Da xuat du lieu ra file json")
#del du lieu file json
def del_data():
    id_del = input("Nhap vao Id can xoa: ")
    data_new = [sv for sv in data if sv["id"] != id_del]
    with open("dulieuhs.json","w",encoding= "utf-8") as f:
        json.dump(data_new,f,indent=4)
        print("Da xoa id {}".format(id_del))
#search data
def student_search(data):
    id_student_search = input("Hay nhap vao 'id' cua sinh vien can tra: ")
    if any(hs["id"] == id_student_search for hs in data ):
        for hs in data:
            if hs["id"] == id_student_search:
                hs_obj = Student.from_dict(hs)
                hs_obj.showInfo()
    else:
        print("ID khong ton tai")
#********************************************************


while True:
    key =''
    data = read_data()
    id_menu = int(input('************MENU**************\n1:Nhap du lieu hoc sinh\n2:Xoa du lieu cua hoc sinh\n3:Tra cuu du lieu cua 1 hoc sinh\n4:In toan bo ho so\n5:Thoat\nLua Chon Chuc Nang:'))
    print("-" * 200)
    if id_menu == 1:
        while True:
            if key == 'E':
                break
            else:
                input_data()
            key = input("Nhap vao 'E' de thoat")
    elif id_menu == 2:
        while True:
            if key == 'E':
                break
            else:
                del_data()
            key = input("Nhap vao 'E' de thoat")
    elif id_menu == 3:
        while True:  
            if key == 'E':
                break
            else:
                student_search(data)
            key = input("Nhap vao 'E' de thoat")
    elif id_menu == 4:
        for sv in data:
            sv_obj = Student.from_dict(sv)
            sv_obj.showInfo()
            print("*"*90)
    elif id_menu == 5:
        break
              

