'''
Create an ATM System
Task1 => Display the balance
Task2 => User Validation (Same) if Yes go to Task3 
Task3 => Options -> task1, cash withdrawal + task1, cash diposit + task1 ,min_Statement of Last 3 Transations
                    card renewal
'''

from Balance import Balance1
from Validation import Validation1

class ATM:
    def __init__(self):
        print("Welcome to CRT Bank of India\n\n1. RuPay\n2. Visa\n3. Master Card")
        while True:
            UserCard = input("Select Your Card : ").lower()
            if UserCard in ['1', 'rupay']:
                UserCard = "RuPay Card"
                UserBalance=Validation1.UserValidation(UserCard)
                break
            elif UserCard in ['2', 'visa']:
                UserCard = "Visa Card"
                UserBalance=Validation1.UserValidation(UserCard)
                break
            elif UserCard in ['3', 'master card']:
                UserCard = "Master Card"
                UserBalance=Validation1.UserValidation(UserCard)
                break
            else:
                print("Invalid Option Boss, Try Again\n")

            
            while True:
              print("CRT Bank of India Operations are \n1. Bank Balance \n2. Cash Withdrawal \n3. Cash Deposit \n4. Bank Statement")
              UserOperation = input("Enter Your Option : ").lower()
              if UserOperation in ['1', 'bank balance']:
                  Balance1.BankBalance(UserBalance)
              elif UserOperation in ['2', 'cash withdrawal']:
                  print("withdrawal ")
              elif UserOperation in ['3', 'cash deposit']:
                  print("deposit ")
              elif UserOperation in ['4', 'bank statement']:
                  print("statement ")
              else:
                  print("Invalid Option Boss, Try Again")


# Main program
ATM()


