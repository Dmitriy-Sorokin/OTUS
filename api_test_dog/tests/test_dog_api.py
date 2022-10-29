import pytest
from requests import Response
from api_test_dog.utils.api import Dog_api
from api_test_dog.utils.assertions import Checking


def test_dog_list():
    print("dog_list status code")
    result_get: Response = Dog_api.dog_random()
    Checking.dog_status_code_assert(result_get, 200)
    Checking.dog_field_assert(result_get, ["message", "status"])
    Checking.gog_value_field_assert(result_get, "status", "success")

