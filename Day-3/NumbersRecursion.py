def count(num):
    if(num ==0) : return 0
    else : 
        return 1 + count(num//10)
print("Count of Digits : ",count(123))


def summ(num):
    if(num ==0) : return 0
    else : return num%10 + summ(num//10)
print("Sum of Digits : ",summ(123))