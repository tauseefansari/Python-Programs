n=int(input("Enter Limit : "))
n1=0
n2=1
print(n1," ",n2, end=" ")
while((n-2)>0):
    n3=n1+n2
    print(n3, end=" ")
    n1=n2
    n2=n3
    n-=1
