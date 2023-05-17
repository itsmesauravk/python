def matrix():
    matrix=[[1,1,1],[1,1,1],[1,1,1]]
    row=int(input("enter row :"))
    column=int(input("enter cloumn : "))
    matrix[row][column]="x"
    for row in matrix:
        for i in row :
            print(i,end=" ")
        print()

        
