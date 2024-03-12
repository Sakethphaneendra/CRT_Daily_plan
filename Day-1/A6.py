"""
To check the type of triangle were 3 inputs are taken and classify it according 
1.Equilateral Triangle
2.Isosceles Triangle
3.Acute Triangle

"""

A1 = int(input("Enter Angle of Side A :"))
A2 = int(input("Enter Angle of Side B :"))
A3 = int(input("Enter Angle of Side C :"))

print(A1,A2,A3)

if A1==A2==A3:
    print("Equilateral Triangle")

elif (A1==A2 and A1==A3) or (A2==A1 and A2==A3) or (A3==A1 and A3==A2):
    print("Isosceles Triangle")
else:
    print("Scalint")