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
    print(
        f"\nCreate square side a={square.side1}, b={square.side2}, c={square.side3},"
        f" d={square.side4}, name {square.name}")


"""Test area square"""


def test_area_square():
    square = Square(2, 4, 2, 4, "Square")
    assert square.area == 8
    print(f"\nArea square = {square.area}")


"""Test perimetr square"""


def test_perimetr_square():
    square = Square(4, 6, 4, 6, "Boby")
    assert square.perimetr == 20
    print(f"\nPerimetr = {square.perimetr}")


"""""Adding up the areas of square"""""


def test_add_area_square():
    square = Square(2, 4, 2, 4, "Square")
    square1 = Square(4, 6, 4, 6, "Boby")
    assert square.add_area(square1) == 32
    print(f"\nSum of areas {square.add_area(square1)}")
