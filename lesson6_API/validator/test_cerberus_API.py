import cerberus
import requests

def test_api_json_schema(base_url):
    """проверка структуры ответа на запрос"""
    respons = requests.get("https://petstore.swagger.io/v2/user/andrey")
    print(respons.json())

    schema = {
        'id': {"type": "number"},
        'username': {"type": "string"},
        'firstName': {"type": "string"},
        'lastName': {"type": "string"},
        'email': {"type": "string"},
        'password': {"type": "string"},
        'phone': {"type": "string"},
        'userStatus': {"type": "number"},
    }

    v = cerberus.Validator()
    assert v.validate(respons.json(), schema)
