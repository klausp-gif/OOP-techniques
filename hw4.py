import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point({self.x}, {self.y})'

    def is_on_x_axis(self):
        return self.y == 0
    
    def is_same_as(self, other):
        return self.x == other.x and self.y == other.y
    
    def distance_from(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
    
    def is_in_unit_circle(self):
        return self.distance_from(Point(0,0)) <= 1
    
    def midpoint(self, other):
        mid_x = (self.x + other.x) / 2
        mid_y = (self.y + other.y) / 2
        return Point(mid_x, mid_y)

p1 = Point(0.5, 0.5)
p2 = Point(1, 0)    

print(p1)                 
print(p1.is_on_x_axis())           
print(p2.is_on_x_axis())           
print(p1.is_same_as(p2))           
print(p1.distance_from(p2))        
print(p1.is_in_unit_circle())      
print(p1.midpoint(p2))             
    
