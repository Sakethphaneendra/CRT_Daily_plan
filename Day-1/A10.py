n = int(input("Enter an Number : "))

for i in range (2,n/2):  
    if(n%i==0):
        print("Not a Prime Number")  
        break
print("Completed")
