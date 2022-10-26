import pytest


@pytest.fixture(params=["s", "d", "f"], ids=["solt", "dot", 'fire'])
def param_fixture(request):
    return request.param


@pytest.fixture(scope="session")
def base_url():
    return 'https://petstore.swagger.io/v2/user/'
