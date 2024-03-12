num = int(input("Enter an Number : "))
i=1
sum=0
while(i<=num/2):
    if(num%i==0):
        print(i,"",end=" ")
        sum=sum+i
    i+=1
    
print("\nSum of ",sum)

