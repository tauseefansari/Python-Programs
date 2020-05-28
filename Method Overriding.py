import math as m
class Sphere:
    def __init__(self,r):
        self.r=r
    def volume(self):
        print("Volume of Sphere : ",((4/3)*m.pi*self.r*self.r*self.r))
class Cube(Sphere):
    def __init__(self,s):
        self.s=s
    def volume(self):
        print("Volume of Cube : ",self.s*self.s*self.s)
rad=float(input("Enter Radius : "))
side=float(input("Enter Side : "))
sp=Sphere(rad)
sp.volume()
cu=Cube(side)
cu.volume()
