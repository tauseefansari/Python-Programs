a=int(input("Enter a Number : "))
for i in range(2,a):
	if a%i==0:
		print(a," is Not Prime")
		break
	else:
		print(a," is Prime")
		break