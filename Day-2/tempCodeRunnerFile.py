num = 8
for i in range(0,num):
    for s in range(num,i,-1):
        print("  ",end=" ")
    for j in range(0,i):
        
        if(i%2==0):
            print("   * ",end=" ")
        else:
            print("   0 ",end=" ")

    print()
print()