import pytest
import requests


# Example with single parameter
@pytest.mark.parametrize("param", [1, 2, 3, 4])
def test_one(param):
    assert param % 2 == 0


# Example with double parameter
@pytest.mark.parametrize("param1", [1, 2, 3, 4])
@pytest.mark.parametrize("param2", [5, 6, 7, 8])
def test_one(param1, param2):
    assert (param1 + param2) % 3 == 0


@pytest.mark.parametrize('userid', ("s", "d", "f", pytest.param("w", marks=pytest.mark.skip("JIRA-12344"))),
                         ids=["negative", "zero", "letter", "skip"])
def test_api_empty_response_on_user_id(userid):
    r = requests.get('https://petstore.swagger.io/v2/user/' + userid, )
    print(r.json())
    assert r.status_code == 404


def test_fixture(param_fixture):
    r = requests.get('https://petstore.swagger.io/v2/user/' + param_fixture, )
    print(r.json())
    assert r.status_code == 200
