matrix1=[]
matrix2=[]
result=[]
print("\t\t\tMatrix 1")
r=int(input("Enter Number of Rows : "))
c=int(input("Enter Number of Columns : "))
for i in range(0,r):
    t=[]
    for j in range(0,c):
        t.append(int(input("Enter Element : ")))
    matrix1.append(t)
print("\t\t\tMatrix 2")
r2=int(input("Enter Number of Rows : "))
c2=int(input("Enter Number of Columns : "))
for i in range(0,r2):
    t=[]
    for j in range(0,c):
        t.append(int(input("Enter Element : ")))
    matrix2.append(t)
print("\t\t\tResult")
for i in range(0,r):
    t=[]
    for j in range(0,c2):
        t.append(matrix1[i][j]+matrix2[i][j])
    result.append(t)
for i in range(len(result)):
    for j in range(len(result[i])):
        print(result[i][j],end="\t")
    print()
