def digits(num):
    if(num<=0) : return 0
    else : 
        print(num%10,end=", ")
        digits(num//10)
digits(int(input("Enter a Number : ")))

