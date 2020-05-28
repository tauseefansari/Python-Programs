class MethodOverloading:
    def area(self,a,b=None):
        if b==None:
            print("Area of Square : ",a*a)
        elif a!=None and b!=None:
            print("Area of Rectangle : ",a*b)
obj=MethodOverloading()
obj.area(2)
obj.area(5,4)
