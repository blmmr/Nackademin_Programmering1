class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

r1 = Rectangle(5,10)
print(r1.length)
print(r1.width) 
print(r1.area())