from src.Shape import Shape


class Square(Shape):

    def __init__(self, side1, side2, side3, side4, name):
        super().__init__(name)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.side4 = side4

    @property
    def area(self):
        return self.side1 * self.side2

    @property
    def perimetr(self):
        return self.side1 + self.side2 + self.side3 + self.side4


