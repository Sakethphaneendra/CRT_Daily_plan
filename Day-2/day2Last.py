num2 = num = 1578
sum = 0
n=0
while (num2!=0):
    n+=1
    num2 = num2//10

while(num!=0):
    temp = num%10
    sum = sum + pow(temp,n)
    n-=1
    num = num//10
print(sum)

