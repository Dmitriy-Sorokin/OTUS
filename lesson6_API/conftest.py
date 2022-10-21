# content of conftest.py
import pytest
import requests

# def pytest_addoption(parser):
#     parser.addoption(
#         "--cmdopt", action="store", default="type1", help="my option: type1 or type2"
#     )
#
#
# @pytest.fixture
# def cmdopt(request):
#     return request.config.getoption("--cmdopt")

def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://httpbin.org/",
        help="This is request url"
    )
    parser.addoption(
        "--method",
        default="get",
        choices=["get", "post", "put", "putch", "delete"],
        help="method to execute"
    )

@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")

@pytest.fixture
def request_method(request):
    return getattr(request, request.config.getoption("--method"))
