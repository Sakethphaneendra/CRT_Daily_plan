# Starting File :: 
# Creating Registartion file
import os
from CodingHubLog import *


class CODING:
    
    def page1(self):
       
        LR=CodingHubs()
        os.system('cls')
        print("\n\t\t\tWelcome to CodingHub Platform \n ")
        print("1.Login \n2.Register \n")
        while(True):
          UserOption = input("Enter Your Option : ")
          if UserOption in ['1', 'login','Login']:LR.Login();break
          elif UserOption in ['2', 'register','Register']:LR.Registartion();break
          else:
              print("Invalid Option Try Agin : ") 


       

cc= CODING()
# CODING()
cc.page1()



 


