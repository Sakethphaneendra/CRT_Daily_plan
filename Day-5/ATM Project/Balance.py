class Balance1:
    def __init__(self):
        self.Balance = 0
        self.ATMBALANCE=1000000
    
    def Deposite(self, UserCard, UserName):
        if UserCard == "RuPay Card":
            self.Balance = 100000
        elif UserCard == "Visa Card":
            self.Balance = 150000
        elif UserCard == "Master Card":
            self.Balance = 200000
        print("Hello", UserName, " Your", UserCard, " Balance was Rs.", self.Balance)
        return self.Balance
    def BankBalance(self,UserBalance):
        print("Balance in the bank is Rs.", UserBalance)


    
   
        # Your existing code for Deposite method

   



