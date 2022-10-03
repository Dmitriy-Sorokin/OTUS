from src.rectangle import Rectangle


def test_create_rectangle():
    rectangle = Rectangle(4, 5)
    assert isinstance(rectangle, Rectangle)
    assert rectangle.name == "Rectangle"
    assert rectangle.width == 4
    assert rectangle.height == 5

    
def test_perimeter_rectangle():
    rectangle = Rectangle(4, 5)
    assert rectangle.perimeter == 18


def test_area_rectangle():
    rectangle = Rectangle(4, 5)
    assert rectangle.area == 20


def test_add_area_to_rectangle():
    rectagnel_one = Rectangle(4, 5)
    rectangle_two = Rectangle(5, 4)
    assert rectagnel_one.add_area(rectangle_two) == 40
