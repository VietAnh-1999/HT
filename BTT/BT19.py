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
    
    def getAccountNumber(self):
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
        
class Bank:
    def __init__(self):
        self.List_Bankaccount = []

    def addAccount(self,account):

        self.List_Bankaccount.append(account)

def main():
    bank = Bank()
    acc1 = BankAccount(123456,"VA1999")
    acc2 = BankAccount(456789556,"VA20001")
    
    bank.addAccount(acc1)
    bank.addAccount(acc2)
    for acc in bank.List_Bankaccount:
        print(acc)
    

if __name__ == "__main__":
    main()