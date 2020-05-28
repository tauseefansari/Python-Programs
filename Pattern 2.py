def pattern(n):
    k=1
    for i in range(n):
        for j in range(i):
            print(k, end=" ")
            k+=1
        print("\t")
n=int(input("Enter Number of Rows : "))
pattern(n+1)                    
