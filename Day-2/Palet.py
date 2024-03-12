num2 = num = 1222111
sum=0
print("hi")

while (num!=0):
    temp = num%10
    sum = sum*10 +temp
    num=num//10

print(sum)
if(sum==num2):
    print("Palendrome Number ")
else:
        print("Not Palendrome Number ")


