num1=int(input("Enter First Number : "))
num2=int(input("Enter Second Number : "))
print("GCD of ",num1," and ",num2," is : ", end="")
while(num1 != num2):
    if(num1 > num2):
        num1=num1 - num2
    else:
        num2=num2 - num1
print(num2)
