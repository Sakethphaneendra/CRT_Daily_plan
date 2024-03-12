# #  The integer that is divisable by 
# 3 and 6 print good number,
# 2 and 7 print average number 
# 4 or 9 print Awesome number
# else bad number

number = int(input("Enter an Number : "))


if(number%3==0 and number%6 == 0):
    print("Good Number")
elif(number%2 ==0 and number%7==0):
    print("Average Number")
elif(number%4==0 or number%9==0):
    print("Awesome Number")
else:
    print("bad number")
