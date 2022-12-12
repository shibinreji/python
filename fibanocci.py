def fibonocci(n):
    first=0
    second=1
    count=0
    if(n==1):
        print(first)
    elif(n<=0):
        print("Please enter a positive integer, the given number is not valid!!0")
    else:
        while(count<n):
            print(first)
            third=first+second
            first=second
            second=third
            count+=1
n=int(input("Enter a number:"))
fibonocci(n)