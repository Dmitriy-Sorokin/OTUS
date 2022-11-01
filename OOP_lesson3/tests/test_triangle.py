from OOP_lesson3.src.Triangle import Triangle


def test_create_triangle():
    triangle = Triangle(4, 4, 8, "Равносторонний")
    assert isinstance(triangle, Triangle)
    assert triangle.perimeter == 16
    assert triangle.name == "Равносторонний"
    assert triangle.side1 == 4
    assert triangle.side2 == 4
    assert triangle.side3 == 8
    print(
        f"\n Side A triangle = {triangle.side1}, side b = {triangle.side2}"
        f", side c = {triangle.side3}, name triangle = {triangle.name}")


def test_area_triangle():
    triangle = Triangle(4, 8, 4, "Равносторонний")
    assert triangle.side1 == 4
    assert triangle.side2 == 8
    assert triangle.side3 == 4
    assert triangle.name == "Равносторонний"
    assert triangle.area == 16
    print(f"\nArea = {triangle.area}")


def test_perimetr_triangle():
    triangle = Triangle(8, 8, 16, "Равносторонний")
    assert triangle.side1 == 8
    assert triangle.side2 == 8
    assert triangle.side3 == 16
    assert triangle.perimeter == 32
    print(f"\nPerimetr = {triangle.perimeter}")


def test_add_area_triangle():
    triangle = Triangle(8, 8, 16, "Равносторонний")
    triangle1 = Triangle(4, 8, 4, "Равносторонний")
    assert triangle.add_area(triangle1)
    print(
        f"\nTriangle side a={triangle.side1}, b={triangle.side2}, c={triangle.side3}, "
        f"Triangle1 side a={triangle1.side1}, b={triangle1.side2}, c={triangle1.side3} \nSum of areas = 50")
