class account:

    def get(self,name,acNumber):

        self.name=name
        self.acnumber=acNumber
        self.bal=100

    def withdr(self,withdrr):
        self.bal=self.bal-withdrr
    
    def diposite(self,dip):
        self.bal=self.bal+dip

    def information(self):
         print("Account holder name is: ",self.name)
         print("Account number is: ",self.acnumber)
         print("Account total balance is: ",self.bal)

ac=account()
ac.get(
              name=input("Enter account holder name: "),
              acNumber=int(input("Enter account number"))
          )
while(True):
    print("information: 1.Account information     2.Diposite        3.withdraw   4. Exit ")
    print(" ")
    a=int(input("Enter number: "))

    if a==1:
         ac.information()
          
    elif a==2:
          ac.diposite(
              dip=int(input("Enter amount for diposite: "))
          )
    elif a==3:
              ac.withdr(
              withdrr=int(input("Enter amount for withdraw: "))
          
              )
    elif a==4:
         break
    else:
         print("You do not give valid input")