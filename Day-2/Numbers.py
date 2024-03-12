num1 = int(input("Enter a Number : "))
sum =0
mul=1
print("Reversed Value of Digits is : ",end="")

while (num1!=0):
    temp = num1%10
    rev =temp
    sum= sum+temp
    mul = mul*temp
    print(rev, end="")
    num1 = num1//10

print("\nMultiplication of Digits is : ",mul)
print("Sum of Digits is : ",sum)










# rev = 1
# print("Reversed Number is : ",end="")
# while (num1!=0):
#     temp = num1%10
#     rev =temp
#     print(rev, end="")
#     num1 = num1//10
# print()


# print("Multiplication of Digits is : ",end="")
# # Multiplication
# mul = 1
# while (num2!=0):
#     temp = num2%10
#     mul = mul*temp
#     num2 = num2//10
# print(mul)
# #Sum

# print("Sum of Digits is : ",end="")
# sum = 0
# while (num3!=0):
#     temp = num3%10
#     sum = sum +temp
#     num3 = num3//10
# print(sum)