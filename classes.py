import math

#intro to object orientated programming
class apple():
    def __init__(self, weight, col, crisp, vol):
        self.weight = weight
        self.col = col
        self. crisp = crisp
        self.vol = vol

class Circle():
    def __init__(self, r):
        self.r = r
    
    def area(self):
        return pow(self.r, 2)*math.pi

circle = Circle(2)
print(circle.area())

class Triangle():
    def __init__(self, b, h):
        self.b = b
        self.h = h
    
    def area(self):
        return self.b*self.h/2

triangle = Triangle(10,5)
print(triangle.area())

class Hexagon():
    def __init__(self, sideL):
        self.sideL = sideL
    
    def calculate_perimeter(self):
        return self.sideL*6

hex = Hexagon(10)
print(hex.calculate_perimeter())

#four pillars of object orientated programming


class Shape():    
    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape):
    def __init__(self, l, w):
        self.w = w
        self.l = l
    
    def calculate_perimeter(self):
        return self.w*self.l

class Square(Shape):
    def __init__(self, l):
        self.l = l
    
    def calculate_perimeter(self):
        return pow(self.l,2)

    def change_size(self, num):
        self.l += num

sq = Square(10)
rect = Rectangle(10,20)
sqPer = sq.calculate_perimeter()
rectPer = rect.calculate_perimeter()
sqWAI = sq.what_am_i()
rectWAI = rect.what_am_i()

class Horse():
    def __init__(self, breed, name, rider):
        self.breed = breed
        self.name = name
        self.rider = rider
class Rider():
    def __init__(self, name):
        self.name = name


rider = Rider("slimJim Johnny")    
horse = Horse("mustang", "greg", rider)
print(horse.rider.name)

#more on object orientated programming

class Square2():
    square_list = []
    def __init__(self,l):
        self.l = l
        self.square_list.append(self.l)
    
    def __repr__(self):
        return "{} by {} by {} by {}".format(self.l,self.l,self.l,self.l)

square1 = Square2(10)
square2= Square2(20)
print(Square2.square_list)
print(square1)

def same_same(ob1, ob2):
    return ob1 is ob2

print(same_same("a", "a"))

#Bringing it all together

