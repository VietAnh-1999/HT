import random

def Chao(Ho,Ten):
    print("Xin chao:"+ Ho + Ten)

#Chao("Nguyen"," Anh")

# truyen nhieu doi so ma khong xac dinh trc so luong
# def tkb(*Monhoc):
#     i=1
#     for x in Monhoc:
#         print("Mon hoc {}: {}".format(i,x))
#         i +=1
# tkb("Van","Su",'Dia','1','2','3','4','5','+6')
# list_1 = {"2","Van","Su",'Dia','1','2','3','4','5','+6'}
# i = 0
# while True:
    
#     if i < 20:
#         ran = random.choice(list(list_1))
#         print(ran)
#         i +=1
#     elif i==20:
#         break
List_1 = []
i = 0
while True:
    try:
        n = int(input("Nhap vao gia tri phan tu thu {} cho chuoi: ".format(i)))
        if n < 0:
            break
        else:
            List_1.append(n)
            i += 1
    except:
        print("Phai nhap vao so nguyen")
print(List_1)
# Ham tinh tong
def tinhtong(list):
    tong = sum(List_1)
    return tong
# ham tim max

print(tinhtong(List_1))
print(max(List_1))
print(min(List_1))
