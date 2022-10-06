from src.Shape import Shape


class Rectangle(Shape):

    def __init__(self, side1, side2, side3, side4, name):
        super().__init__(name)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.side4 = side4

    def square(self):
        square = self.side1 * self.side2
        return square

    def perimetr(self):
        perimetr = self.side1 + self.side2 + self.side3 + self.side4
        return perimetr


rectangle = Rectangle(4, 8, 4, 8, "прямоугольник")

print(rectangle.name)
print(rectangle.square())
print(rectangle.perimetr())
