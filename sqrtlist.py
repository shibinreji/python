a=[]
r=int(input("Enter the range"))
print("Enter the elements")
for i in range(0,r):
    a.append(int(input()))
print(a)
b=[]
for i in a:
    b.append(i**2)
print(b)
