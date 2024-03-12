n = int(input("Enter an Number : "))

for i in range (2,n):
    if(n%i==0):
        print("Not a Prime Number",end="--> ")  
        break
      
print("Done")
       

