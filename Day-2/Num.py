num2 = num = int(input("Enter a Number : "))

c =0
while(num!=0):
    c = c+1
    num = num//10
sum=0
num = num2
while(num!=0):
    temp = num%10
    sum = sum + pow(temp,c)
    num = num//10

print(sum)

if(sum==num2):
    print("Armstrong number")
    print(2^6)
else:
    print("Not ArmStrong Number ")
    print(2^6)
