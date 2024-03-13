def count(num):
    if(num ==0) : return 0
    else : return 1 + count(num//10)
def ArmStrong(n,c):
    if (n==0):return 0
    else : return pow(n %10,c) + ArmStrong(n//10,c)
num = int(input("Enter a Number : "))
print(ArmStrong(num,count(num)))
if(ArmStrong(num,count(num)) == num):print("ArmStrong Number")
else: print("Not ArmStrong Number")