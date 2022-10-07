from src.Shape import Shape
import math


class Circle(Shape):

    def __init__(self, radius, name):
        super().__init__(name)
        self.radius = radius

    @property
    def square(self) -> int:
        return math.pi * (self.radius ** 2)

    @property
    def perimetr(self) -> int:
        return 2 * math.pi * self.radius


circle = Circle(10, "круг")

# print(circle.name)
# print(f"Радиус {circle.radius}"
print(int(circle.square))
