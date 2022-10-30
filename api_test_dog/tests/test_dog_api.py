import pytest
from requests import Response
from api_test_dog.utils.api import Dog_api
from api_test_dog.utils.assertions import Checking


def test_dog_list():
    print("Check dog_list status code, fields, fields value")
    result_get: Response = Dog_api.dog_list()
    Checking.dog_status_code_assert(result_get, 200)
    Checking.dog_field_assert(result_get, ["message", "status"])
    Checking.gog_value_field_assert(result_get, "status", "success")
    print("Successful")

def test_dog_images():
    print("Check dog_list status code, fields, fields value")
    result_get: Response = Dog_api.dog_images()
    Checking.dog_status_code_assert(result_get, 200)
    Checking.dog_images_cerberus(result_get)
    Checking.gog_value_field_assert(result_get, "status", "success")
