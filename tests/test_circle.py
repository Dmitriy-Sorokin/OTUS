from src.Circle import Circle

'''Create circle'''


def test_create_circle():
    circle = Circle(8, "КРУГ")
    assert isinstance(circle, Circle)
    assert circle.radius == 8
    assert circle.name == "КРУГ"


"""Test area circle"""


def test_area_circle():
    circle = Circle(8, "КРУГ")
    assert circle.area == 201.06192982974676


"""Test perimetr circle"""


def test_perimetr_circle():
    circle = Circle(10, "Gig BRO")
    assert circle.perimetr == 62.83185307179586


"""Adding up the areas of circle"""


def test_add_area_circle():
    circle = Circle(8, "КРУГ")
    circle1 = Circle(10, "Gig BRO")
    assert circle.add_area(circle1) == 515
