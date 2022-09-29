from src.Shape import Shape


class Triangle(Shape):
    side1 = None
    side2 = None
    side3 = None

    def __init__(self, side1, side2, side3, area, name, perimeter):
        super(Triangle, self).__init__(area, name, perimeter)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3


triangle = Triangle(1, 2, 3, 4.5, "triangle", 5)

print(triangle.side1)
print(triangle.side2)
print(triangle.side3)
print(triangle.area)
print(triangle.name)
print(triangle.perimeter)
