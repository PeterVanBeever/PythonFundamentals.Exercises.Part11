class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        area = self.length * self.width
        return area
    
    def perimeter(self):
        perimeter = ((self.length + self.width) * 2)
        return perimeter

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

