# create a class of name placements which has a function info() which displays the num of placements 673 + still counting. create an other class name department with function diplay which would display the names of dept in college 
# cse,eee,ece,mech,it create the class pragati with the function welcome which diplays the message welcome to pragati engiinerng colege we are glad to have you onboarded and should also display the details about depts, and placements

class Placements:
    def __init__(self):
        print("=> The Total number of placements in Pragati are '678 and still counting..' ")

class Departments(Placements):
    def __init__(self):
        Placements()
        print("=> Branches we have \n   1.CSE \n   2.ECE\n   3.MECHNICAL\n   4.EEE\n   5.IT\n   6.CSE(DS)\n")

class Pragati(Departments):
    def __init__(self):
        s="Pragati Engineering College".upper()
        print("=> Welcome to",s,"\n=> We are Have on your Onboarding process.")
        Departments()

Pragati()