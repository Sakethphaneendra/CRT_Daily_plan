'''
#create a class "ticket" which will be the abstract class 
#inside that create a function "book ticket" which will be the abstract method and hasnothing in it.
#create a class "makemytrip" which will use the 'bookticket function' from "ticket" classto take the details such as 
#name, ph no, email id,journey date and displays a message saying Thsnk u from bookingfrom makemytrip.
#create a class "irctc" which uses the 'bookticket' of "ticket" class and takes the samedetails as makemytrip but 
#in the end it will give an option to user to select whether it is one way or round trip
#if the user option is round trip it again asks the user to enter the return date as well and then prints a message 
#thank u for choosing irctc else it prints a message thank u for choosing irctc.
#create a class indigo which takes all the details as irctc and just asks which mode of transport u want to go in 
#train ,bus or flight and displays a message thank u for choosing indigo
'''

from abc import ABC,abstractclassmethod

# from Oops2 import Departments
# Departments()

class ticket(ABC):
    a=2.12
    @abstractclassmethod
    def bookTicket():pass

class makemytrip(ticket):

    def bookTicket():
        print("\nWelcome to MakeMyTrip ")
        print("Please Enter The Details to Continue : \n")
        name = input("1.Name : ")
        number = input("2.Phone Number : ")
        email = input("3.Email Address : ")
        journey_date = input("4.Jouney Date : ")
        print("\nThank You,",name,"for choosing MakeMyTrip")

class irctc(ticket):
      def bookTicket():
        print("\nWelcome to IRCTC ")
        print("Please Enter The Details to Continue : \n")
        name = input("1.Name : ")
        number = input("2.Phone Number : ")
        email = input("3.Email Address : ")
        # select whether it is one way or round trip
        while(True):
            trip = input("4.Type of Trip (1.One way or 2.Round trip )").lower()
            if(trip=='2' or trip=="round trip"):
                journey_date = input("4.Jouney Date : ")
                return_date = input("4.Return Date : ");break
            elif(trip=='1' or trip=="one way"):
                journey_date = input("4.Jouney Date : ");break
            else:
                print("Invalid Option Boss, Try Again")
    
        print("\nThank You,",name,"for choosing IRCTC")


class indigo(ticket):
      def bookTicket():
        print("\nWelcome to Indigo ")
        print("Please Enter The Details to Continue : \n")
        name = input("1.Name : ")
        number = input("2.Phone Number : ")            
        email = input("3.Email Address : ")
        # select whether it is one way or round trip
        while(True):
            trip = input("4.Type of Trip (1.One way or 2.Round trip ) : ").lower()
            if(trip=='2' or trip=="round trip"):
                journey_date = input("4.Jouney Date : ")
                return_date = input("4.Return Date : ");break
            elif(trip=='1' or trip=="one way"):
                journey_date = input("4.Jouney Date : ");break
            else:
                print("Invalid Option Boss, Try Again")
        # #train ,bus or flight
        while(True):
            Transport = input("4. Type of Trip (1.Train or 2.Bus or 3.Flight ) : ").lower()
            if(trip=='1' or trip=="train" or trip=='2' or trip=="bus" or trip=='3' or trip=="flight"):
                break
            else:
                print("Invalid Option Boss, Try Again\n")
        print("\nThank You,",name,"for choosing INDIGO ")

print("\n\n\t\t\t\t\tWelcome to Smark Booking Services \nOur Special Partners :: \n \n1.MakeMytrip \n2.Irctc\n3.Indigo \n ")
while(True):
    value = input("Enter Your Choose : ").lower()
    if(value=='1' or value=="makemytrip"):makemytrip.bookTicket();break
    elif(value=='2' or value=="irctc"):irctc.bookTicket();break
    elif(value=='3' or value=="indigo"):indigo.bookTicket();break
    else:print("Invalid Option Boss, Try Agin")


