num = 6
for i in range (0,num):
    for s in range(num,i,-1):
        print("  ",end="")

    for j in range(0,i):
        print("   *",end="")
    print()

for i in range (num,0,-1):
    for s in range(num,i,-1):
         print("  ",end="")

    for j in range(0,i):
        print("   *",end="")
    print()


  
