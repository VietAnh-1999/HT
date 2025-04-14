# Khai bao class
class SoHoc:
    # Khai bao thuoc tinh
    def __init__(self):
        self.__number1 = 0
        self.__number2 = 0

    # Phương thức Thuộc tính
    def inputInfo(self):
        self.__number1 = float(input("Nhap vao so nguyen 1: "))
        self.__number2 = float(input("Nhap vao so nguyen 2: "))

    def printInfo(self):
        print("Gia tri so thu nhat duoc la: {}".format(self.__number1))
        print("Gia tri so thu hai duoc la: {}".format(self.__number2))

    def addition(self):
        add_number = self.__number1 + self.__number2
        return add_number
    
    def subtract(self):
        sub_number = self.__number1 - self.__number2
        return sub_number
    
    def multi(self):
        multi_number = self.__number1 * self.__number2
        return multi_number
    def division(self):
        if self.__number2 != 0:
            div_numner = self.__number1 / self.__number2
            return div_numner
        else:
            return "Khong the chi cho '0'"


#main
xulyso = SoHoc()
xulyso.inputInfo()
xulyso.printInfo()
print(xulyso.addition())
print(xulyso.subtract())
print(xulyso.division())