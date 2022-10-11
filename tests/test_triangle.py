import pytest
from src.Triangle import Triangle


def test_create_triangle():
    triangle = Triangle(4, 4, 8, "Равносторонний")
    assert triangle.perimeter == 16
    assert triangle.name == "Равносторонний"
    assert triangle.side1 == 4
    assert triangle.side2 == 4
    assert triangle.side3 == 8


def test_square_triangle():
    triangle = Triangle(4, 8, 4, "Равносторонний")
    assert triangle.side1 == 4
    assert triangle.side2 == 8
    assert triangle.side3 == 4
    assert triangle.name == "Равносторонний"
    assert triangle.square == 16


def test_perimetr_triangle():
    triangle = Triangle(8, 8, 16, "Равносторонний")
    assert triangle.side1 == 8
    assert triangle.side2 == 8
    assert triangle.side3 == 16
    assert triangle.perimeter == 32
