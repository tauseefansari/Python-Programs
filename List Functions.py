l=[]
for x in range(5):
    l.append(input("Enter an Element of List : "))
a=input("Enter What to Be Count : ")
print("Count  is : ",l.count(a))
l2=["abc","ghi","lmn"]
l.extend(l2)
print("After Extend List : ",l)
b=input("Enter an Element to be Search : ")
print("Element Found at Index : ",l.index(b)+1)
x=input("Enter Element to be Insert : ")
y=int(input("Enter Position : "))
l.insert(y-1,x)
print("After Insertion : ",l)
z=int(input("Enter Position of Element to be Remove : "))
l.pop(z+1)
l.remove(input("Enter Element to be Removed : "))
l.reverse()
print("Reverse List : ",l)
l.sort()
print("Sorted List : ",l)
