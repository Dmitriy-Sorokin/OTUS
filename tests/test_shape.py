import pytest
from src.Shape import Shape
from src.Triangle import Triangle


def test_create_base_shape():
    with pytest.raises(Exception):
        Shape("Паралелепипед")


def test_add_area_triangle():
    triangle = Triangle(4, 4, 8, "Равнастаронний треугольник")
    not_shape = 0
    with pytest.raises(ValueError):
        triangle.add_area(not_shape)
