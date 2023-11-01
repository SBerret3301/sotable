def soutable(T,a,b):
    s = []
    for i in range(a,b):
        s.append(T[i])
    return s

T = []
for i in range(10):
    print("enter the element number",i+1,":")
    x = float(input())
    T.append(x)
a = int(input("enter the first index :"))
b = int(input("enter the second index :"))
print(soutable(T,a,b))