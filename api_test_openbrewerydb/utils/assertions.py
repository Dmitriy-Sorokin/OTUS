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
        checked_js = response
        checked_field_value = checked_js.get(field_name)
        print("Value field getting")
        assert checked_field_value == expected_value
        print(expected_value + ' The value is correct!!!')

        '''Checked field by using cerberus'''

    @staticmethod
    def assert_list_breweries_cerberus(response: Response):
        resp = response.json()[0]
        print(resp['id'])
        schema = {
            'id': {"type": "string"},
            'name': {"type": "string"},
            'brewery_type': {"type": "string"},
            'street': {"type": "string"},
            'address_2': {"type": "string", 'nullable': True},
            'address_3': {"type": "string", 'nullable': True},
            'city': {"type": "string"},
            'state': {"type": "string"},
            'county_province': {"type": "string", 'nullable': True},
            'postal_code': {"type": "string"},
            'country': {"type": "string"},
            'longitude': {"type": "string"},
            'latitude': {"type": "string"},
            'phone': {"type": "string"},
            'website_url': {"type": "string", 'nullable': True},
            'updated_at': {"type": "string"},
            'created_at': {"type": "string"}
        }
        v = cerberus.Validator()
        assert v.validate(response.json()[0], schema)

    @staticmethod
    def range_array_3_page(response: Response):
        checked = response.json()
        print(len(checked))
        assert len(checked) == 3

    @staticmethod
    def json_schema_by_city(response: Response):
        """проверка структуры ответа на запрос"""
        resp = response.json()[0]
        schema = {
            "type": "object",
            "properties": {
                'id': {"type": "string"},
                'name': {"type": "string"},
                'brewery_type': {"type": "string"},
                'street': {"type": "string"},
                'address_2': {"type": "null"},
                'address_3': {"type": "null"},
                'city': {"type": "string"},
                'state': {"type": "string"},
                'county_province': {"type": "null"},
                'postal_code': {"type": "string"},
                'country': {"type": "string"},
                'longitude': {"type": "string"},
                'latitude': {"type": "string"},
                'phone': {"type": "string"},
                'website_url': {"type": "string"},
                'updated_at': {"type": "string"},
                'created_at': {"type": "string"}
            },
            "required": ["id", "name", "brewery_type", "street", "city", "state", "postal_code",
                         "country", "longitude", "latitude", "phone", "website_url", "updated_at", "created_at",
                         "address_2", "address_3", "county_province"]
        }

        validate(instance=response.json()[0], schema=schema)

        assert resp["id"] == "10-barrel-brewing-co-san-diego"
        assert resp["name"] == "10 Barrel Brewing Co"
        assert resp["street"] == "1501 E St"
        assert resp["city"] == "San Diego"
        assert resp["state"] == "California"
        assert resp["postal_code"] == "92101-6618"
        assert resp["country"] == "United States"
        assert resp["longitude"] == "-117.129593"
        assert resp["latitude"] == "32.714813"
        assert resp["phone"] == "6195782311"
        assert resp["website_url"] == "http://10barrel.com"
        assert resp["updated_at"] == "2022-10-30T06:11:39.514Z"
        assert resp["created_at"] == "2022-10-30T06:11:39.514Z"



