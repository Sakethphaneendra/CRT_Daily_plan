# Calc the diff of sum of sums that are divisble by 6 and !6 in the range of first 30 numbers

# SUm 
sum1=sum2=0
for i in range(1,30+1):
    if(i%6==0):
       sum1 = sum1+i
    else:
        sum2 = sum2+i

print(-(sum1-sum2))