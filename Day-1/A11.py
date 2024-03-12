''' Calc the sum of digits of a number '''

n = int(input("Enter a Number : "))
sum=0
while n != 0 :
    temp = n%10
    sum =sum+ temp

    n= int((n/10))

print(sum)
231.21222
