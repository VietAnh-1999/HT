class BankAccount:
    def __init__(self, accountNumber, accountName, balance=0):
        self.accountNumber = accountNumber
        self.accountName = accountName
        self.balance = balance

    def getAccountNumber(self):
        return self.accountNumber

    def getAccountName(self):
        return self.accountName

    def getBalance(self):
        return self.balance

    def deposit(self, money):
        if money > 0:
            self.balance += money
            return True
        return False

    def withdrawMoney(self, money):
        if 0 < money <= self.balance:
            self.balance -= money
            return True
        return False


class Bank:
    def __init__(self):
        self.listBankAccount = []

    def searchAccountNumber(self, accountNumber):
        for i, acc in enumerate(self.listBankAccount):
            if acc.getAccountNumber() == accountNumber:
                return i
        return -1

    def getTotal(self):
        return len(self.listBankAccount)

    def getItem(self, accountNumber):
        index = self.searchAccountNumber(accountNumber)
        if index != -1:
            return self.listBankAccount[index]
        return None

    def addAccount(self, accountNumber, accountName):
        if self.searchAccountNumber(accountNumber) != -1:
            return False
        newAccount = BankAccount(accountNumber, accountName)
        self.listBankAccount.append(newAccount)
        return True

    def depositMoney(self, accountNumber, money):
        index = self.searchAccountNumber(accountNumber)
        if index != -1:
            return self.listBankAccount[index].deposit(money)
        return False

    def withdrawMoney(self, accountNumber, money):
        index = self.searchAccountNumber(accountNumber)
        if index != -1:
            return self.listBankAccount[index].withdrawMoney(money)
        return False

    def removeAccount(self, accountNumber):
        index = self.searchAccountNumber(accountNumber)
        if index != -1:
            del self.listBankAccount[index]
            return True
        return False

    def showAllAccounts(self):
        if not self.listBankAccount:
            print("Không có tài khoản nào trong hệ thống.")
        else:
            for acc in self.listBankAccount:
                print(f"Số tài khoản: {acc.getAccountNumber()} | Tên: {acc.getAccountName()} | Số dư: {acc.getBalance():,.0f} VNĐ")


def main():
    bank = Bank()

    while True:
        print("\n====== MENU QUẢN LÝ TÀI KHOẢN NGÂN HÀNG ======")
        print("1. Thêm tài khoản mới")
        print("2. Nạp tiền vào tài khoản")
        print("3. Rút tiền khỏi tài khoản")
        print("4. Xóa tài khoản")
        print("5. Hiển thị thông tin tất cả tài khoản")
        print("6. Kiểm tra thông tin tài khoản")
        print("7. Thoát")
        choice = input("Chọn chức năng (1-7): ")

        if choice == "1":
            acc_num = input("Nhập số tài khoản: ")
            acc_name = input("Nhập tên tài khoản: ")
            if bank.addAccount(acc_num, acc_name):
                print("✅ Tạo tài khoản thành công.")
            else:
                print("❌ Tài khoản đã tồn tại.")

        elif choice == "2":
            acc_num = input("Nhập số tài khoản: ")
            money = float(input("Nhập số tiền muốn nạp: "))
            if bank.depositMoney(acc_num, money):
                print("✅ Nạp tiền thành công.")
            else:
                print("❌ Nạp tiền thất bại. Kiểm tra số tài khoản.")

        elif choice == "3":
            acc_num = input("Nhập số tài khoản: ")
            money = float(input("Nhập số tiền muốn rút: "))
            if bank.withdrawMoney(acc_num, money):
                print("✅ Rút tiền thành công.")
            else:
                print("❌ Rút tiền thất bại. Kiểm tra số dư và số tài khoản.")

        elif choice == "4":
            acc_num = input("Nhập số tài khoản cần xóa: ")
            if bank.removeAccount(acc_num):
                print("✅ Xóa tài khoản thành công.")
            else:
                print("❌ Không tìm thấy tài khoản.")

        elif choice == "5":
            bank.showAllAccounts()

        elif choice == "6":
            acc_num = input("Nhập số tài khoản cần kiểm tra: ")
            acc = bank.getItem(acc_num)
            if acc:
                print(f"Tài khoản: {acc.getAccountNumber()}, Tên: {acc.getAccountName()}, Số dư: {acc.getBalance():,.0f} VNĐ")
            else:
                print("❌ Không tìm thấy tài khoản.")

        elif choice == "7":
            print("✅ Thoát chương trình.")
            break

        else:
            print("❌ Lựa chọn không hợp lệ. Vui lòng chọn từ 1-7.")

if __name__ == "__main__":
    main()