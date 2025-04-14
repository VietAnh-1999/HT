# tạo 1 dictionary

sinhvien = {
    "Ho ten" : "Nguyen Viet Anh",
    "Tuoi": "19",
    "Ma lop" : "DH01",
    "Diem trung binh" : "10"
}
print(sinhvien)
print(sinhvien["Ho ten"])

#/////////////////////
print("******************************************************")
# updte va lay gia tri key
sinhvien["Diem trung binh"] = "9.9"
print(sinhvien)
print(sinhvien.get("Ho ten"))
sinhvien.update({"Ho ten":"Viet Anh", "Diem trung binh" : "9.99999999"})
print(sinhvien)
#########################
print("***************************************************")
# them key
sinhvien["Nam sinh"]  = "1999"
print(sinhvien)
# xoa key
sinhvien.pop('Tuoi')
print(sinhvien)

for x in sinhvien.keys():
    print(x)
print("*************************************")

for x in sinhvien.values():
    print(x)
print("*************************************")
for x,y in sinhvien.items():
    print(x,":",y)