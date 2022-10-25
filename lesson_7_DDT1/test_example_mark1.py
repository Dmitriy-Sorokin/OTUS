import pytest


@pytest.mark.regress
@pytest.mark.skip(reason="This test is broken")
def test_example_one():
    assert 0


@pytest.mark.regress
@pytest.mark.xfail
def test_example_two():
    assert False


@pytest.mark.auth
def test_example_three():
    pass
