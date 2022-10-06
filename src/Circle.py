from src.Shape import Shape
import math


class Circle(Shape):

    def __init__(self, radius, name):
        super().__init__(name)
        self.radius = radius

    def square(self):
        square = math.pi * (self.radius ** 2)
        return square

    def perimetr(self):
        perimetr = 2 * math.pi * self.radius
        return perimetr


circle = Circle(10, "круг")

print(circle.name)
print(f"Радиус {circle.radius}")

