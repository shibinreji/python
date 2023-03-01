class rectangle:
    def __init__(self,len,bre):
        self.l=len
        self.b=bre
    def area(self):
        self.rslt=self.l*self.b
        print("Area={}".format(self.rslt))
    def perimeter(self):
        rslt=(self.l+self.b)*2
        print("Perimeter={}".format(rslt))
        return rslt
length1=int(input("Enter length of rect1:"))
breadth1=int(input("Enter breadth of rect1:"))
length2=int(input("Enter length of rect2:"))
breadth2=int(input("Enter breadth of rect2:"))

obj1=rectangle(length1,breadth1)
obj2=rectangle(length2,breadth2)
a=obj1.area()
obj1.perimeter()

b=obj2.area()
obj2.perimeter()
if(a>b):
    print("The area of object 1 is greater")
else:
    print("The area of object 2 is greater")