l=[]
print("Enter 20 Numbers : ")
for i in range(1,21):
    l.append(int(input("Enter Number %d : "%i)))
t=tuple(l)
print(t[:10])
print(t[11:])