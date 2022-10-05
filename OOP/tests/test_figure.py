import pytest

from src.figure import Figure
from src.rectangle import Rectangle


def test_create_instance_figure():
    with pytest.raises(Exception):
        Figure(2)


def test_add_area_to_not_figure():
    rectangle = Rectangle(4, 5)
    not_figure = 0
    with pytest.raises(ValueError):
        rectangle.add_area(not_figure)