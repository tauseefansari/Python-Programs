m=int(input("Enter From Limit : "))
n=int(input("Enter To Limit : "))
print("Even Numbers From ",m," to ",n," are : ")
if m%2==0:
    for i in range(m,n+1,2):
        print(i, end=" ")
else:
    for i in range(m+1,n+1,2):
        print(i, end=" ")        
