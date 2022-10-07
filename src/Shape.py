class Shape:
    name = None

    def __init__(self, name):
        self.name = name

    def add_area(self, shape):
        if not isinstance(shape, Shape):
            raise ValueError("Фигуры не существует")
        return int(self.square) + int(shape.square)
