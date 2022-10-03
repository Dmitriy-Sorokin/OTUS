from src.circle import Circle


def test_create_circle():
    circle = Circle(7)
    assert isinstance(circle, Circle), f"Circle is not instance class Circle"
    assert circle.name == "Circle", f"Circle has wrong name: {circle.name} but must be 'Circle'"
    assert circle.radius == 7, f"Circle has wrong radius: {circle.radius} but must be '7'"


def test_perimeter_circle():
    circle = Circle(7)
    assert circle.perimeter == 43.982297150257104, f"Circle has wrong perimeter: {circle.perimeter} but must be '43.982297150257104'"


def test_area_circle():
    circle = Circle(7)
    assert circle.area == 153.93804002589985, f"Circle has wrong area: {circle.area} but must be '153.93804002589985'"


def test_add_area_to_circle():
    circle_one = Circle(5)
    circle_two = Circle(7)
    assert circle_one.add_area(
        circle_two) == 232.4778563656447, f"Circle has wrong area after add another circle area: {circle_one.add_area(circle_two)}"
