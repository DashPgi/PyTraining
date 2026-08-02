from symtable import Class


class Shape:
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


class Rectangle(Shape, Color):
    shape = "rectangle"
    Color = Color.red

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


class Square(Shape):
    shape = "square"

    def __init__(self, x):
        self.x = x

    def area(self):
        return self.x * 2

    def perimeter(self):
        return self.x * self.x

    def volume(self):
        return self.x * self.x * self.x

    @staticmethod
    def info():
        print("This Is a Square")


class Shape:
    pass


class Triangle(Shape):
    shape = "triangle"

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    @classmethod
    def equal_sides(cls, side):
        return cls(side, side, side)



R = Rectangle(1, 2, 3)
S = Square(4)
t = Triangle.equal_sides(5)

print(R.area(), R.perimeter(), R.volume(), R.Color)
print(S.area())
print(t.perimeter())

