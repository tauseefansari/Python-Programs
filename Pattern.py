k=7
c=65
for i in range(0,7):
	for j in range(0,k):
		print(end="    ")
	k=k-1
	for j in range(i):
		print("    ",chr(c),end="  ")
		c+=1
	print("\n")