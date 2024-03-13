
def fabo(a,b):
    if(b>=100): return 0
    else :
       sum = a + b 
       a= b
       b=sum
       print(sum, end= " ")
       fabo(a,b)
print("0 1 ",end="")
fabo(0,1)


#  Fabo = 0 1 sum = i +j i=j j= sum
# sum =   (5 * (4 * (3 * (2 * 1))))


# Recursive function for two count the nuber of digits of a number
# to calulate the sum of ditis 


