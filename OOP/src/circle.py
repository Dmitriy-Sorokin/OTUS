import math
from .figure import Figure


class Circle(Figure):
    
    def __init__(self, radius, name="Circle") -> None:
        super().__init__(radius, name)
        self.radius = radius

    @property
    def perimeter(self) -> int:
        return 2 * math.pi * self.radius

    @property
    def area(self) -> int:
        return math.pi * self.radius ** 2
