A = set(input().split())
n = int(input())
dem = 0
for _ in range(n):
    set_1 = set(input().split())
    if A.issuperset(set_1):
        dem += dem
if dem == n:
    print("True")
else:
    print("False")