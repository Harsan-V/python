a = [[" "for i in range(10)]for i in range(10)]  

for i in range(10):
    for j in range(10):
        if(j==0 or j==9):
            a[i][j] = "*"
        if(i==j and i>4):
            a[i][j]="*"
        if(i+j==9 and j<5):
            a[i][j]="*"



for i in range(10):
    for j in range(10):
        print(a[i][j],end=" ")
    print()


    

        

        