from functools import reduce
l=list(range(1,10))
res=reduce(lambda x,y: x*y,l)
print("Multiply of 1-10 : ",res)