from src.Shape import Shape

class Triangle(Shape):
    side1 = None
    side2 = None
    side3 = None

    def __init__(self, side1, side2, side3,  name):
        super().__init__(name)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3


    def square(self):
        area = 0.5 * self.side1 * self.side2
        return area

triangle = Triangle(6, 6, 3,name="triangle")

print(triangle.square())
#
# print(triangle.side1)
# print(triangle.side2)
# print(triangle.side3)

# print(triangle.name)
# print(triangle.perimeter)
