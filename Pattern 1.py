def pattern(n):
    for i in range(n):
        for j in range(i):
            print("*", end=" ")
        print("\t")
n=int(input("Enter Number of Rows : "))
pattern(n+1)
