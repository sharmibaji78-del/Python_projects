from math import sqrt
class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def set_width(self,value):
        self.width = value
    def set_height(self,value):
        self.height = value
    def get_area(self):
        area = self.width * self.height
        return area
    def get_perimeter(self):
        perimeter = 2*(self.width + self.height)
        return perimeter
    def get_diagonal(self):
        diagonal = sqrt(self.width**2 + self.height**2)
        return diagonal
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        result = ""
        for i in range(self.height):
            result += '*' * self.width + '\n'
        return result
    def get_amount_inside(self,shape):
        width_count = self.width // shape.width
        height_count = self.height // shape.height
        return width_count * height_count
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

class Square(Rectangle):
    def __init__(self,side):
        self.side = side
        super().__init__(side,side)
    def set_width(self,value):
        self.width = value
        self.height = value
    def set_height(self, value):
        self.width= value
        self.height = value
    def set_side(self,value):
        self.width= value
        self.height = value
    def __str__(self):
        return f'Square(side={self.width})'
    
rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))

        
