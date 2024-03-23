# __init__(), __str__(), __add__(), __mult__(), __lt__(), __gt__(), __le__()

import math
class cartPoint:
    def __init__(self, a=1, b=1):
        self.x = a
        self.y = b
    def changePoint(self, da, db):
        self.x += da
        self.y += db
    def printOutput(self):
        print(f"The coordinates are {self.x,self.y}")
    def disOrigin(self):
        self.distance = math.sqrt(self.x**2+self.y**2)
        print(f"The distance of the point {self.x, self.y} from the origin is {self.distance}")
    def convPolar(self):
        self.r = math.sqrt(self.x**2 + self.y**2)
        self.theta = math.atan(self.y/self.x)
        print(f"The equivalent polar coordinates are: {self.r:.3f}, {self.theta:.3f}")
    def __str__(self):
        return("I am second object of the class Cartpoint")
    
    def __add__(self, other):
        """This function specifies how two objects must be added and what must be returned """
        return (self.x+other.x, self.y +other.y)

p1 = cartPoint(5,9)
p2 = cartPoint()
p2.printOutput()
print(p2) # OR print(p2.__str__()) <-- Explicit calling
print(p1 + p2)  # OR print(p1.__add__(p2)) <-- Explicit calling

# p1.printOutput()
# p1.changePoint(4,1)
# p1.printOutput()
# p1.disOrigin()
# p1.convPolar()
