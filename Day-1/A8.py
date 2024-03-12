n = int(input("Enter N value : "))
i=0
j=1
print("0 1",end=" ")
sum = i+j

for i in range(2,n):
   
    print(sum, end=" ")
    i=j
    j=sum
    sum=i+j
   

