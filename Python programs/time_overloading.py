class time:
    def __init__(self,hour,minute,sec):
        self.__hr=hour
        self.__min=minute
        self.__sec=sec
    def __add__(self, other):
        tym_hr=self.__hr+other.__hr
        tym_min=self.__min+other.__min
        tym_sec=self.__sec+other.__sec
        if (tym_sec>60):
            tym_min=tym_min+tym_sec//60
            tym_sec=tym_sec%60
        if (tym_min>60):
            tym_hr=tym_hr+tym_min//60
            tym_min=tym_min%60
        print("Total time={}hr:{}min:{}sec".format(tym_hr,tym_min,tym_sec))
print("Enter time in hour min sec format\n")
hour1=int(input("Enter the hour of 1st tym:"))
min1=int(input("Enter minutes of 1st tym:"))
sec1=int(input("Enter seconds of 1st  tym:"))
hour2=int(input("Enter the hour of 2nd tym:"))
min2=int(input("Enter minutes of 2nd tym:"))
sec2=int(input("Enter seconds of 2nd  tym:"))
t1=time(hour1,min1,sec1)
t2=time(hour2,min2,sec2)
t1+t2