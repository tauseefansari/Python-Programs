words=[]
n=int(input("How many Words you want to insert : "))
print("Enter ",n," Words : ")
for i in range(n):
    str=input("Enter Word : ")
    words.append(str)
sort=sorted(words)
print("\nSotred Words : ")
for i in sort:
    print(i)
