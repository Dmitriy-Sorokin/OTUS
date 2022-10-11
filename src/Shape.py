class Shape:
    name = None

    def __init__(self, name):
        if self.__class__ == Shape:
            raise Exception('Can not instantiate abstract base class')
        self.name = name

    def add_area(self, shape):
        if not isinstance(shape, Shape):
            raise ValueError("Фигуры не существует")
        return int(self.square) + int(shape.square)
