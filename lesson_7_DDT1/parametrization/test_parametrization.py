import pytest


# Example with single parameter
@pytest.mark.parametrize("param", [1, 2, 3, 4])
def test_one(param):
    assert param % 2 == 0


# Example with double parameter
@pytest.mark.parametrize("param1", [1, 2, 3, 4])
@pytest.mark.parametrize("param2", [5, 6, 7, 8])
def test_one(param1, param2):
    assert (param1 + param2) % 3 == 0
