# Number is divisable by its sum of digits or not

n2 = n = int(input("Enter a number : "))
sum=0
print(n2)
while (n!=0):
    temp = n%10
    sum= sum +temp
    n= n//10
print(n2%sum)
if n2%sum==0:
    print("It Can")
else:
    print("It can't")
