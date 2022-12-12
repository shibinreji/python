fact=1
num=int(input("Enter a number:"))
if(num<0):
    print("Factorial of negative number does not exist!!")
elif(num==0):
    print("Factorial of 0 is 1")
else:
    for i in range(1,num+1):
        fact=fact*i
    print("Factorial of",num,"is",fact)