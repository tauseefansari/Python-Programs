l=[]
n=int(input("Enter Number of Elements : "))
for i in range(1,n+1):
    l.append(int(input("Enter Element %d : "%i)))
ser=int(input("Enter Element to be Search : "))
for i in range(len(l)):
    if l[i]==ser:
        print("%d is Found at %d"%(l[i],i+1))
        break
else:
    print("%d is Not Found "%l[i])