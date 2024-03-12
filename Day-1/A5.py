# Leap Year or not Conditions : year is %4 & Not %100  or year is %400 leap year

year = int(input("Enter a year : "))

if((year % 4==0 and year %100 !=0) or year % 400 ==0 ):
    print("Leap Year")

else:
    print("Not Leap Year")