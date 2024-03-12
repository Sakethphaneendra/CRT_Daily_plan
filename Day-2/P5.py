row = 4
col = 10

for i in range(1,row):
    for j in range(1,col):
       
        if(i==1 or i==(row-1)):
             print(" * ",end="")
        else:
            if(j==1 or j==col-2):
                print(" * ",end="")
            print("   ",end="")

    print()