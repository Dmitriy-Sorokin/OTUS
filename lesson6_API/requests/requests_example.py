import requests
import json


def test_status_code():
    response = requests.get('https://ya.ru')
    assert response.status_code == 200
