class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def inputInfo(self):
        self.length = float(input("Nhap vao chieu dai: "))
        self.width = float(input("Nhap vao chieu rong: "))

    def dientich(self):
        dientich = self.length * self.width
        return dientich
    
    def chuvi(self):
        chuvi = (self.length + self.width) * 2
        return chuvi


# main
hinh1 = Rectangle(20,60)
hinh2 = Rectangle(50,65)
print(hinh1.chuvi())
print(hinh2.chuvi())
print(hinh1.dientich())

print(hinh2.dientich())