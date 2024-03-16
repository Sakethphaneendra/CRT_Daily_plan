import csv
import os
from homepage import *
class CodingHubs:
    def DataBase(self):
        self.CustomerTable = open("CustomerTable.csv",'a',newline='')
        self.Db =csv.writer(self.CustomerTable)
        # self.Db.writerow(["Email","Password"])
    
    def Registartion(self):
        os.system('cls')
        while(True):
          self.userid = input("Enter Your Email Id : ")
          self.userpass = input("Enter Your Password : ")
          self.reuserpass = input("Re Enter The Password : ")
          if(self.userpass==self.reuserpass):
            print("Registration Succesful")
            # Create the Data in DB
            self.Db.writerow([self.userid,self.userpass])
            break
          else:
             print("Password Not Matching Try Again \n ") 

    def Login(self):
             os.system('cls') 
             print("Login Form")
             while(True):
               self.id = input("Enter Your Email Id : ")
               self.password = input("Enter Your Password : ")
               with open('CustomerTable.csv',"r",newline='') as file:
                      reader=csv.DictReader(file)
                      ld=1
                      for row in reader:
                       if(self.id==row["Email"] and self.password==row["Password"] ):
                          h=Home()
                          h.ProductsPage()
                          break
                       else:print("\n User Not Found Try Again ") 
                     
                        
                         
              
            
            
  

