
# for i in range(0,6):
#     for j in range(0,i):
#         print(i , " ",end="")
#     print()
# for i in range(4,0,-1):
#     for j in range(0,i):
#         print(i , " ",end="")
#     print()


##################################################



# num = 8
# for i in range(0,num):
#     for s in range(num,i,-1):
#         print("  ",end=" ")
#     for j in range(0,i):
        
#         if(i%2==0):
#             print("   * ",end=" ")
#         else:
#             print("   0 ",end=" ")

#     print()
# print()

# num = 6
# for i in range(1,num):
#     print("  "*(num-1), "   *" * i )


#################################################



num = 8
for i in range(0,num):
    for s in range(num,i,-1):
        print(" ",end=" ")
    for j in range(0,i):
         
            if(j<3 and j>8):
              print("")
            else:
              print("  *",end=" ")
            


    print()
print()
