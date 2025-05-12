import json
#tao class BankAcount
class BankAccount:
    def __init__(self,accountNumber,accountName):
        self.accountNumber = accountNumber
        self.accountName = accountName
        self.balance = 0
    def __str__(self):
        return f"Tài khoản: {self.accountNumber},Ten tai khoan: {self.accountName}, Số dư: {self.balance} VNĐ"

    def getAccountNumber(self):
        return self.accountNumber
    
    def getAccountName(self):
        return self.accountName
    
    def getBalance(self):
        return self.balance
    
    def deposit(self,money):
        self.balance += money
        print("Da nap {}đ vao tai khoan".format(money))

    def withdraw(self,money):
        if self.balance > money:
            self.balance -= money
            print("Da rut {}đ tu tai khoan".format(money))
        else:
            print("Tai khoan khong du tien")
    def to_dict(self):
        return{
            'accountName': self.accountName,
            'accountNumber': self.accountNumber,
            'balance': self.balance
        }

class Bank(BankAccount):
    def __init__(self):
        self.List_Bankaccount = []
        BankAccount.__init__()

    def addAccount(self,account):

        self.List_Bankaccount.append(account)

    def search(self,accountNumber):
        for acc in self.List_Bankaccount:
            if acc.accountNumber == accountNumber:
                 print(accountNumber)
        else:
            print("Tai khoan khong ton tai")
    #def getTotal(self):


def write_json(data):
    with open("dulieuNH.json","w",encoding= "utf-8") as f:
        json.dump(data,f,indent=4)
        print("Da xuat du lieu ra file json")

def read_json():
    try:
        with open("dulieuNH.json","r",encoding= "utf-8") as f:
            dt = json.load(f)
            print("Da doc du lieu ra file json")
            return dt
    except FileNotFoundError:
        print("Khong tim duoc file hoac file khong ton tai")
        return []
    except json.JSONDecodeError:
        print("file loi") 
        return []  

def main():
    bank = Bank()
    N = int(input("Nhap vao so tai khoan can tao: "))
    i = 0
    data = read_json()
    print(data)
    while i < N:
        try:
            acc_num = input("Nhap vao acc_number(6 so): ")
            if not acc_num.isdigit():
                print("Vui long chi nhap so")
                continue
            if len(acc_num) != 6:
                print("khac sau ky tu")
                continue

        except KeyboardInterrupt:
            break
        except:
            print("Dinh dang chua dung. Vui long nhap lai")

        try:
            acc_name = input("Nhap vao acc_name(it nhat 8 ky tu): ")
            
            if len(acc_name) < 8:
                print("chua du 8 ky tu")
                continue
        except KeyboardInterrupt:
            break
        except:
            print("Dinh dang chua dung. Vui long nhap lai")

        acc = BankAccount(acc_num,acc_name)
        bank.addAccount(acc)
        data.append(acc.to_dict())
        print(data)
        write_json(data)
        i += 1
    
    for acc in bank.List_Bankaccount:
        print(acc)
    

if __name__ == "__main__":
    main()