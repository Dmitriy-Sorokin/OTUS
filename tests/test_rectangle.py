from src.Rectangle import Rectangle

"""Create rectangle"""


def test_create_rectangle():
    rectangle = Rectangle(4, 2, 4, 2, "Прямоугольник")
    assert isinstance(rectangle, Rectangle)
    assert rectangle.name == "Прямоугольник"
    assert rectangle.side1 == 4
    assert rectangle.side2 == 2
    assert rectangle.side3 == 4
    assert rectangle.side4 == 2


"""Test square rectangle"""


def test_area_rectangle():
    rectangle = Rectangle(4, 2, 4, 2, "Прямоугольник")
    assert rectangle.area == 8


"""Test perimetr rectangle"""


def test_perimetr_rectangle():
    rectangle = Rectangle(6, 4, 6, 4, "Прямоугольный дядя Вася")
    assert rectangle.perimetr == 20


'''Adding up the areas of rectangles'''


def test_add_area_rectangle():
    rectangle = Rectangle(6, 4, 6, 4, "Прямоугольный дядя Вася")
    rectangle2 = Rectangle(4, 2, 4, 2, "Прямоугольник")
    assert rectangle.add_area(rectangle2) == 32
