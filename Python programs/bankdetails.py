class bankacc:
    def __init__(self,name,accnum,acctype):
        self.name=name
        self.accno=accnum
        self.acctyp=acctype
        balance=0
        self.bal=balance
    def deposit(self):
        dep=int(input("Enter deposit amount:"))
        self.dep=dep
        self.bal=self.bal+self.dep
        print("Successfully credited to account,new balance in acc is:{}".format(self.bal))
    def withdraw(self):
        amount = int(input("Enter withdrawal amount:"))
        self.witd=amount
        if(self.witd>self.bal):
            print("INSUFFICIENT AMOUNT")
        else:
            self.bal=self.bal-self.witd
            print("Rupees {} withdrawn from account,new balance is {}".format(self.witd,self.bal))
name=raw_input("Enter your name:")
accnum=int(input("Enter your acc num:"))
acctype=raw_input("Enter your acc type:")
obj1=bankacc(name,accnum,acctype)
obj1.deposit()
obj1.withdraw()
