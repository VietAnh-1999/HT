import numpy
N = int(input())
A = []
# def nhap():
#     try:
#         row = list(map(float,input().split()))
#         if len(row) != N:
#             raise ValueError("Ban phai nhap dung {0} phan tu cho moi dong".format(N))
#     except ValueError:
#         print("Vui long nhap so")
#         row=nhap()
#     return row
        
for _ in range(N):
   while True:
        try:
            row = list(map(float,input().split()))
            if len(row) != N:
                print("Ban phai nhap dung {0} phan tu cho moi dong".format(N))
                continue
            A.append(row)
            break
            
        except ValueError:
            print("Vui long nhap so")
            
    
print(numpy.linalg.det(A))