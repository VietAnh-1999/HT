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
            tuoi = int(input('Nhap vao tuoi cua sinh vien co "id": {} : '.format(self._id) ))
            if tuoi >= 18:
                self.tuoi = tuoi
                break
            else:
                print("vui long nhap tuoi cho hoc sinh lon hon 18!")
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
# main *************************************************************************************************************************************************************************
Hocsinh = Student()
data = []
def read_data():
    try:
        with open("dulieuhs.json","r",encoding= "utf-8") as f:
            data = json.load(f)
            return data
        print("Da doc duoc du lieu")
    except FileNotFoundError:
        print("File khong ton tai")
    except json.JSONDecodeError:
        print("File json rong hoac khong ton tai")
    

def input_data():
    Hocsinh.inputInfo()
    Hocsinh.showInfo()
    data.append(Hocsinh.to_dict())
    with open("dulieuhs.json","w",encoding= "utf-8") as f:
        json.dump(data,f,indent=4)
        print("Da xuat du lieu ra file json")

#def del_data():
def student_search():
    read_data()
    id_student_search = input("Hay nhap vao 'id' cua sinh vien can tra")
    if any(HS["id"] == id_student_search for HS in data ):
        for HS in data:
            if HS["id"] == id_student_search:
                HS_obj = Student.from_dict(HS)
                HS_obj.showInfo()


    


while True:

    id_menu = int(input('************MENU**************\n1:Nhap du lieu hoc sinh\n2:xoa du lieu cua hoc sinh\n3:Tra cuu du lieu cua 1 hoc sinh\n4:Thoat\nLua Chon Chuc Nang:'))
    if id_menu == 1:
        read_data()
        input_data()
    # elif id_menu == 2:
    elif id_menu == 3:
        student_search()
    elif id_menu == 4:
        break
              

