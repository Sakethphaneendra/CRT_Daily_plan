from Balance import Balance1

class Validation1:
    def UserValidation(UserCard):
        print("Login System\n")
        while True:
            UserName = input("Enter Your Username : ")
            UserPassword = input("Enter Your Password : ")
            if UserName == UserPassword:
                balance_instance = Balance1()  # Create an instance of Balance1
                balance = balance_instance.Deposite(UserCard, UserName)  # Call Deposite method
                break
            
            else:
                print("Invalid UserName/Password Boss, Try Again : ")

# Calling the UserValidation method
