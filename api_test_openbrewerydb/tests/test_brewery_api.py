from api_test_openbrewerydb.utils.api_brewery import Brewery
from api_test_openbrewerydb.utils.assertions import Assert
import pytest
from requests import Response


def test_single_brewery():
    print("\nCheck dog_list status code, fields, fields value")
    get_result: Response = Brewery.single_brewery()
    Assert.assert_status_code(get_result, 200)
    Assert.assert_expected_field(get_result, ["id", "name", "brewery_type", "street", "address_2", "address_3",
                                              "city", "state", "county_province", "postal_code", "country",
                                              "longitude", "latitude", "phone", "website_url", "updated_at",
                                              "created_at"])
    Assert.assert_value_field(get_result, "id", "madtree-brewing-cincinnati")
    Assert.assert_value_field(get_result, "name", "MadTree Brewing")
    Assert.assert_value_field(get_result, "brewery_type", "regional")
    Assert.assert_value_field(get_result, "street", "3301 Madison Rd")

