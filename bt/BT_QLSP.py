import json

class product:
    def __init__(self):
        self.name_pr = ""
        self.desciption = ""
        self.price = 0
        self.rate = 0

    def get_namePR(self):
        return self.name_pr
    
    def addProduct(self):
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
        pr.addProduct()
        self.ProductList.append(pr)
        print(self.ProductList)
        data.append(pr.to_dict())
        with open("product.json","w",encoding="utf-8")as f:
            json.dump(data,f,indent=4)


        
#    def removeProduct():
    



#*******************************************************************
data=[]
def read_data_json():
        try:
            with open ("product.json","r",encoding="utf-8")as f:
                data = json.load(f)
                return data           
        except FileNotFoundError:
            print("file khong to tai")
        except json.JSONDecodeError:
            print("file json rong hoac khong ton tai")
read_data_json()
print(data)
Shop_1 = Shop()
Shop_1.addProduct(data)
    
        