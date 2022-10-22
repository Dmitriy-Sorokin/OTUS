import requests
from jsonschema import validate


def test_api_json_schema():
    """проверка структуры ответа на запрос"""
    respons = requests.get("https://petstore.swagger.io/v2/user/andrey")
    response = respons.json()
    print(respons.json())

    schema = {
        "type": "object",
        "properties": {
            'id': {"type": "number"},
            'username': {"type": "string"},
            'firstName': {"type": "string"},
            'lastName': {"type": "string"},
            'email': {"type": "string"},
            'password': {"type": "string"},
            'phone': {"type": "string"},
            'userStatus': {"type": "number"},
        },
        "required": ["id", "username", "firstName", "lastName", "email", "password", "phone", "userStatus"]
    }

    validate(instance=respons.json(), schema=schema)

    assert response["id"] == 9222968140497274388
    assert response["username"] == "andrey"
