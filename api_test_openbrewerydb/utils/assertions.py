import json
from requests import Response
import requests
import cerberus
from jsonschema import validate

'''Methods for checking the responses of our requests'''


class Assert:
    '''Checking status code'''

    @staticmethod
    def assert_status_code(response: Response, status_code):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print(f"Successful status code: " + str({response.status_code}))
        else:
            print(f"Wrong status code: " + str({response.status_code}))


    '''Method for checking presence of required fields in response to request'''

    @staticmethod
    def assert_expected_field(response: Response, expected_field):
        field = json.loads(response.text)
        assert list(field) == expected_field
        print("All field present")

        '''Method for checking value of required fields in response to request '''

    @staticmethod
    def assert_value_field(response: Response, field_name, expected_value):
        checked = response.json()
        checked_field_value = checked.get(field_name)
        assert checked_field_value == expected_value
        print(expected_value + ' TRUE !!!')

        '''Checked field by using cerberus'''
    @staticmethod
    def assert_list_breweries(response: Response):
        schema = {
            'id': {"type": "list"},
            'name': {"type": "string"},
            'brewery_type': {"type": "string"},
            'street': {"type": "string"},
            'address_2': {"type": "string"},
            'address_3': {"type": "string"},
            'city': {"type": "string"},
            'state': {"type": "string"},
            'county_province': {"type": "string"},
            'postal_code': {"type": "string"},
            'country': {"type": "string"},
            'longitude': {"type": "string"},
            'phone': {"type": "string"},
            'website_url': {"type": "string"},
            'updated_at': {"type": "string"},
            'created_at': {"type": "string"},
            'latitude': {"type": "string"},
        }

        v = cerberus.Validator()
        assert v.validate(response.json(), schema)

