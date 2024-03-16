
class dummy:
    class D1:
        def dd(self):
            self.a=123
            print("Hello")
            ss=dummy.D2()
            ss.d()
    class D2:
        def d(self):
            print("World")
        
class dummychild(dummy):
    sss=dummy.D1()
    def sas(sel):
        print(sss.a)
sss = dummy()
obj1 = sss.D1()
obj2 = sss.D2()
obj1.dd()
dc = dummychild()
dc.sas()


# Inheritance Types   
# Single inheritance, Multiply inheritance, Multi-level inheritance, Hybrid Inheritance


# create a class of name placements which has a function info() which displays the num of placements 673 + still counting. create an other class name department with function diplay which would display the names of dept in college 
# cse,eee,ece,mech,it create the class pragati with the function welcome which diplays the message welcome to pragati engiinerng colege we are glad to have you onboarded and should also display the details about depts, and placements