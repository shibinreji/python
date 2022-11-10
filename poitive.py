a=[]
n=int(input("Enter the limit"))
print("Enter the " +str(n)+" numbers")
for i in range(0,n):
    ele=int(input())
    a.append(ele)
print(a)
b=[]
for i in a:
    if i>=0:
        b.append(i)
print(b)
        
