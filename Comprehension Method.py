import math
numbers=[x for x in range(11)]
print("Numbers from 0-10 : ",numbers)
odds=[x for x in range(1,11,2)]
print("Odd Numbers : ",odds)
even=[x for x in range(0,11,2)]
print("Even Numbers : ",even)
fact=[math.factorial(x) for x in range(11)]
print("Factorial of Numbers : ",fact)
squares=[x**2 for x in range(11)]
print("Squares of Numbers : ",squares)
