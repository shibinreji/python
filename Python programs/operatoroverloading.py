class rectangle:
    def __init__(self,len,bred):
        self.__l=len
        self.__b=bred
    def area(self):
        self.rslt=self.__l*self.__b
        print("Area={}".format(self.rslt))
    def __lt__(self,other):
        return self.area()< other.area()
length1=int(input("Enter length of rect1:"))
breadth1=int(input("Enter breadth of rect1:"))
length2=int(input("Enter length of rect2:"))
breadth2=int(input("Enter breadth of rect2:"))

obj1=rectangle(length1,breadth1)
obj2=rectangle(length2,breadth2)
if(obj1<obj2):
    print("The area of rectangle 2 is greater")
else:
    print("The area of rectangle 1 is greater")