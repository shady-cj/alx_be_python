class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")
    
class Rectangle(Shape):
    
    def __init__(self, width, length):
        self.width = width
        self.length = length
    
    def area(self):
        return self.length * self.width
    
class Square(Shape):
    
    def __init__(self, size):
        self.size = size
    
    def area(self):
        return self.size * self.size
    
class Circle(Shape):
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        import math
        return math.pi * (self.radius ** 2)



