from src.Square import Square

'''Create square'''


def test_create_square():
    square = Square(2, 4, 2, 4, "Square")
    assert isinstance(square, Square)
    assert square.side1 == 2
    assert square.side2 == 4
    assert square.side3 == 2
    assert square.side4 == 4
    assert square.name == "Square"


"""Test area square"""


def test_area_square():
    square = Square(2, 4, 2, 4, "Square")
    assert square.area == 8


"""Test perimetr square"""


def test_perimetr_square():
    square = Square(4, 6, 4, 6, "Boby")
    assert square.perimetr == 20


"""""Adding up the areas of square"""""


def test_add_area_square():
    square = Square(2, 4, 2, 4, "Square")
    square1 = Square(4, 6, 4, 6, "Boby")
    assert square.add_area(square1) == 32
