a={"Apple","Mango","Unknown"}
b={"Google","Apple","Unknown"}
print(a)
a.add(input("Enter Name of Fruit : "))
print(a)
print("Number of Items : ",len(a))
a.update(b)
print("Updated : ")
print(a)
print("Subset  : ",b.issubset(a))
print("Superset : ",a.issuperset(b))
print("Difference : ",a.difference(b))
print("Intersection : ",a.intersection(b))
print("Union : ",a.union(b))
print("Disjoin : ",a.isdisjoint(b))
a.clear()
print("Clear : ")
print(a)

