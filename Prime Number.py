num=int(input("Enter a Number : "))
for i in range(2,num):
    if num%i==0:
        print(num," is Not a Prime Number")
        break
    else:
        print(num," is a Prime Number")
        break
