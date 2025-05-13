import json

class product:
    def __init__(self):
        self.name_pr = ""
        self.desciption = ""
        self.price = 0
        self.rate = 0

    def get_namePR(self):
        return self.name_pr
    
    def addProduct_1(self):
        self.name_pr = input("Nhap vao ten cua san pham:  ")
        self.desciption = input("Nhap vao mo ta cho san pham {} :  ".format(self.name_pr))
        while True:
            try:
                print("Gia phai nho hon 100")
                price = float(input("Nhap vao gia cho san pham {}: ".format(self.name_pr)))
                if 0 < price < 100 :
                    self.price = price
                    break
                else:
                    print("Nhap gia khong thanh cong")
            except:
                print("Nhap sai dinh dang! vui long nhap lai")

        while True:
            try:
                print("Nhap vao danh gia cho san pham (voi  muc do hai long tu 1--->5)")
                rate = float(input())
                if 0 <= rate<= 5:
                    self.rate = rate
                    break
                else:
                    print("Nhap danh gia khong thanh cong")
            except:
                print("Dinh dang khong dung! Vui long nhap lai")

    def viewInfo(self):
        print("name: {}".format(self.name_pr))
        print("description: {}".format(self.desciption))
        print("price: {}".format(self.price))
        print("List rate: {}".format(self.rate))

    def to_dict(self):
        return{
            "name":self.name_pr,
            "desciption":self.desciption,
            "price":self.price,
            "lissRate":self.rate
        }
    @staticmethod
    def from_dict(data):
        prd =product()
        prd.name_pr = data["name"]
        prd.desciption = data["desciption"]
        prd.price = data["price"]
        prd.rate = data["lissRate"]
        return prd
class Shop:
    def __init__(self):
        self.ProductList = []

    def addProduct(self,data):
        pr = product()
        pr.addProduct_1()
        self.ProductList.append(pr)
        print(self.ProductList)
        data.append(pr.to_dict())
        with open("product.json","w",encoding="utf-8")as f:
            json.dump(data,f,indent=4)

    @staticmethod
    def sort_price(data):
        spr_sort_price = dict(sorted(data.items(),key = lambda item: item[1]["price"]))
        print(spr_sort_price)
        


    @staticmethod
    def SearchProduct(data):
        try:
            print("Nhap vao khoang gia can tra cuu")
            Prod_search_1 = int(input("Nhap vao gioi han gia tren: "))
            Prod_search_2 = int(input("Nhap vao gioi han gia duoi: "))
            print("Danh sach  product  loc duoc")
            print("-"*60)
            if any(dt for dt in data if Prod_search_2 < dt["price"] < Prod_search_1):
                data_search = [dt for dt in data if Prod_search_2 < dt["price"] < Prod_search_1]
                for spr in data_search:
                    sprd = product.from_dict(spr)
                    sprd.viewInfo()
                    print("*"*20)
            else:
                print("Khong ton tai san pham trong khoang gia")
            print("-"*60)
        except:
            print("Nhap sai dinh dang")

    @staticmethod
    def removeProduct(data):
        prod_del = input("Nhap vao ten san pham can xoa: ")
        if any(dt for dt in data if dt["name"] == prod_del):
            data_new = [dt for dt in data if dt["name"] != prod_del]
            with open(r"D:\5.HT\HT\bt\product.json","w",encoding="utf-8") as f:
                json.dump(data_new,f,indent= 4)
                print("Da xoa san pham {} ra khoi danh sach".format(prod_del))
        else:
            print("San pham khong ton tai trong danh sach")

    



#*******************************************************************
data=[]
def read_data_json():
    try:
        with open(r"D:\5.HT\HT\bt\product.json","r",encoding="utf-8") as f:
            data = json.load(f)
            return data           
    except FileNotFoundError:
        print("file khong to tai")
    except json.JSONDecodeError:
        print("file json rong hoac khong ton tai")
Shop_1 = Shop()
data = read_data_json()
#**********************************************************
for sp in data:
    prd = product.from_dict(sp)
    prd.viewInfo()
    print("*"*50)
#**********************************************************
while True:
    print("1: Add new product")
    print("2: Remove product")
    print("3: Search product")
    print("4: SortProduct")
    print("5: Exit")
    while True:
        try:
            key = int(input("Nhap lua chon: "))
            if 0 < key < 6 :
                break
            else:
                print("Nhap lua chon khong dung. Vui long nhap lai!")
        except:
            print(" Sai dinh dang. Vui long nhap lai!")
#***********************************************************
    if key == 1: 
        Shop_1.addProduct(data)
    elif key == 2:
        Shop.removeProduct(data)
    elif key == 3:
        Shop.SearchProduct(data)
    elif key == 4:
        Shop_1.sort_price(data)
    elif key == 5:
        break
        
        