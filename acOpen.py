class HDFC:
      
      def __init__(self,name,acnum,bal):
           self.bal=bal
           self.name=name
           self.acnum=acnum
      
          
      def withdra(self,withAmount):
           self.bal-=withAmount
           print("Now Your balance is: ",self.bal)
           print("")
      def diposit(self,dipamount):
           self.bal+=dipamount
           print("Now Your balance is: ",self.bal)
           print(" ")
      def information(self):
           print("Account Holder name is: ",self.name)
           print("Account Number is: ",self.acnum)
           print("Now Your balance is: ",self.bal)


class SBI:
      
      def __init__(self,name,acnum,bal):
           self.bal=bal
           self.name=name
           self.acnum=acnum
      
          
      def withdra(self,withAmount):
           self.bal-=withAmount
           print("Now Your balance is: ",self.bal)
           print("")
      def diposit(self,dipamount):
           self.bal+=dipamount
           print("Now Your balance is: ",self.bal)
           print(" ")
      def information(self):
           print("Account Holder name is: ",self.name)
           print("Account Number is: ",self.acnum)
           print("Now Your balance is: ",self.bal)
        
          
a=input("choose the name of the bank in whome account is open SBI or HDFC: ")

if a=="HDFC" or "hdfc":
    hd=HDFC(
         name=input("Enter custmer name: "),
         acnum=int(input("Enter Account number: ")),
         bal=int(input("How much money are you depositing now?: "))
         )

    while(True):
        print("Enter choice for: ....")
        print("1.Persional Information     2. Withdraw     3. Diposite     4.exit  ")
        choice=input(": ")
    
        if choice==1:
             hd.information()
    
        elif choice==2:
             hd.withdra(
                  withAmount=int(input("Enter ammount for withdra: "))
             )
        elif choice==3:
             hd.diposit(
                  dipamount=int(input("Enter ammount for Diposite"))
             )
              
        elif choice==4:
             break
        
        else:
             print("Invlid choice")
elif a=="SBI" or "sbi":
    sb=SBI(
         name=input("Enter custmer name: "),
         acnum=int(input("Enter Account number: ")),
         bal=int(input("How much money are you depositing now?: "))
         
    )
    while(True):
        print("Enter choice for: ....")
        print("1.Persional Information     2. Withdraw     3. Diposite     4.exit  ")
        choice=input(": ")
    
        if choice==1:
             sb.information()
    
        elif choice==2:
             sb.withdra(
                  withAmount=int(input("Enter ammount for withdra: "))
             )
        elif choice==3:
             sb.diposit(
                  dipamount=int(input("Enter ammount for Diposite"))
             )
              
        elif choice==4:
             break
        
        else:
             print("Invlid choice")