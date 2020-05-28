def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
print("\t 1:Addition \t\t\t 2:Subtraction")
print("\t 3:Multiplication \t\t 4:Division")
option=int(input("Enter Option : "))
num1=int(input("Enter First Number : "))
num2=int(input("Enter Second Number : "))
if option==1:
    print("Addition of ",num1," and ",num2," is : ",add(num1,num2))
elif option==2:
    print("Subtraction of ",num1," and ",num2," is : ",sub(num1,num2))
elif option==3:
    print("Multiplication of ",num1," and ",num2," is : ",mul(num1,num2))
elif option==4:
    print("Division of ",num1," and ",num2," is : ",div(num1,num2))
else:
    print("Invalid Option")
