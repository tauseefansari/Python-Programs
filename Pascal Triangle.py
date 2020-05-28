n=int(input("Enter Number of Rows : "))
l=[1]
fl=[]
for i in range(n):
	fl.append(l)
	newl=[]
	newl.append(l[0])
	for i in range(len(l)-1):
		newl.append(l[i]+l[i+1])
	newl.append(l[-1])
	l=newl
k=(len(fl))
for i in range(0,len(fl)):
	for j in range(0,k):
		print(end="   ")
	k=k-1
	for j in range(len(fl[i])):
			print("  ",fl[i][j],end="  ")
	print("\r")