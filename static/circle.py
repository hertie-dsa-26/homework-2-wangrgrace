import math

class Circle:
    def __init__(self, radius): # two parameters: object itself and the radius of the circle
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius # 2πr

    def area(self):
        return math.pi * self.radius ** 2 # πr²