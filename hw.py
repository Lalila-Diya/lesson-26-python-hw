import math

class Circle:
    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        return math.pi*(self.radius**2)
    def cicumference(self):
        return math.pi*(self.radius)*2
    def diametere(self):
        return self.radius*2
    
circle=int(input("Enter the radius: "))
u=input("Enter the unit")
print("Area:",circle.area(),"sq.",u)
print("Circumference:",circle.cicumference(),u)
print("Diametere:",circle.diametre(),u)