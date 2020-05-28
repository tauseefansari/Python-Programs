stack=[]
n=int(input("Enter Size of Stack : "))
for i in range(1,n+1):
    stack.append(int(input("Enter %d Element of Stack : "%i)))
print(stack)
print("Pop Element : %d"%stack[-1])
stack.pop()
print(stack)
