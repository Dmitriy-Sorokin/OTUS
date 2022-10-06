from src.Shape import Shape


class Triangle(Shape):

    def __init__(self, side1, side2, side3, name):
        super().__init__(name)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def square(self):
        square = 0.5 * self.side1 * self.side2
        return square

    def perimeter(self):
        perimetr = self.side1 + self.side2 + self.side3
        return perimetr


triangle = Triangle(6, 6, 3, name="triangle")

print(triangle.square())
print(triangle.perimeter())
