from src.Shape import Shape


class Triangle(Shape):

    def __init__(self, side1, side2, side3, name):
        super().__init__(name)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    @property
    def area(self) -> int:
        return (self.side1 * self.side2) * 0.5

    @property
    def perimeter(self) -> int:
        return self.side1 + self.side2 + self.side3

