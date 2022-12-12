list=[]
sum=0
num=int(input("Enter how many element you wantto put in the list:"))
for i in range(0,num):
     a=int(input("Enter the numbers:"))
     list.append(a)
for i in range(0,len(list)):
    sum=sum+list[i]
print(list)
print("Sum of all elements in the list is",sum)