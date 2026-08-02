from abc import ABC, abstractmethod
from enum import Enum

# need for abstraction....

class Shape(ABC):
    def ELEMENT(self, metal):
        self.metal = metal

    def area(self):
        pass

    def perimeter(self):
        pass

    def volume(self):
        pass


class Color:
    red = "red"
    green = "green"
    blue = "blue"
    white = "white"
    black = "black"
    class codecolor(Enum):
        RED = "FF0000"
        GREEN = "00FF40"
        BLUE = "0004FF"

    def __init__(self, color):
        self.color = color

    def __len__(self):
        return len(self.color)


class Rectangle(Shape, Color):
    shape = "rectangle"
    Color = Color.red

    def __call__(self):
        return "This Class Isn't Class Anyway"

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def area(self):
        return self.x * self.y

    def perimeter(self):
        return (self.x + self.y) * 2

    def volume(self):
        return self.x * self.y * self.z

    @property
    def Persianname(self):
        return "Moraba"


class Square(Shape):
    shape = "square"

    def __str__(self):
        return "This Square have an area and Perimetr and also Volume"

    def __repr__(self):
        return f"This Square have jus one width : {self.x}"

    def __init__(self, x):
        self.x = x

    def area(self):
        return self.x ** 2

    def perimeter(self):
        return self.x * 4

    def volume(self):
        return self.x * self.x * self.x

    @staticmethod
    def info():
        print("This Is a Square")


class Triangle(Shape, Color):
    shape = "triangle"  # public
    _shape = "have a 3 different line"  # protected (need object to show itself)
    __shape = "it is 2D shape"  # private(need a method to show itself)

    def __init__(self, a, b, c, metal):
        super().ELEMENT(metal)
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    @classmethod
    def equal_sides(cls, side):
        return cls(side, side, side, Color.white)


C = Color(["red", "green", "blue", "white", "black"])
R = Rectangle(1, 2, 3)
S = Square(4)
T = Triangle(1, 2, 3, "metalic")
t = Triangle.equal_sides(5)


print(R.area(), R.perimeter(), R.volume(), R.Color)
print(S.area())
print(t.perimeter())
print(T.metal)
print(S)
print(repr(S))
print(len(C))
print(R())
print(R.Persianname)