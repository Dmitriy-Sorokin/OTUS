from src.Shape import Shape
import math


class Circle(Shape):

    def __init__(self, radius, name):
        super().__init__(name)
        self.radius = radius

    @property
    def area(self) -> int:
        return math.pi * (self.radius ** 2)

    @property
    def perimetr(self) -> int:
        return 2 * math.pi * self.radius
