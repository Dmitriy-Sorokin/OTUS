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
    Assert.assert_value_field(get_result, "city", "Cincinnati")
    Assert.assert_value_field(get_result, "state", "Ohio")
    Assert.assert_value_field(get_result, "postal_code", "45209-1132")
    Assert.assert_value_field(get_result, "country", "United States")
    Assert.assert_value_field(get_result, "longitude", "-84.4239715")
    Assert.assert_value_field(get_result, "latitude", "39.1563725")
    Assert.assert_value_field(get_result, "phone", "5138368733")
    Assert.assert_value_field(get_result, "website_url", "http://www.madtreebrewing.com")
    Assert.assert_value_field(get_result, "updated_at", "2022-10-30T06:11:39.514Z")
    Assert.assert_value_field(get_result, "created_at", "2022-10-30T06:11:39.514Z")


def test_lest_breweries():
    print("\nCheck dog_list status code, fields, fields value")
    get_result: Response = Brewery.list_breweries()
    one_object_resp = get_result.json()[0]
    Assert.assert_status_code(get_result, 200)
    Assert.assert_list_breweries_cerberus(get_result)
    Assert.range_array_3_page(get_result)
    Assert.assert_value_field(one_object_resp, "id", "10-56-brewing-company-knox")
    Assert.assert_value_field(one_object_resp, "name", "10-56 Brewing Company")
    Assert.assert_value_field(one_object_resp, "brewery_type", "micro")
    Assert.assert_value_field(one_object_resp, "street", "400 Brown Cir")
    Assert.assert_value_field(one_object_resp, "city", "Knox")
    Assert.assert_value_field(one_object_resp, "state", "Indiana")
    Assert.assert_value_field(one_object_resp, "postal_code", "46534")
    Assert.assert_value_field(one_object_resp, "country", "United States")
    Assert.assert_value_field(one_object_resp, "longitude", "-86.627954")
    Assert.assert_value_field(one_object_resp, "latitude", "41.289715")
    Assert.assert_value_field(one_object_resp, "phone", "6308165790")
    Assert.assert_value_field(one_object_resp, "updated_at", "2022-10-30T06:11:39.514Z")
    Assert.assert_value_field(one_object_resp, "created_at", "2022-10-30T06:11:39.514Z")


def test_by_city():
    print("\nCheck dog_list status code, fields, fields value")
    get_result: Response = Brewery.filter_breweries_by_city()
    Assert.assert_status_code(get_result, 200)
    Assert.json_schema_by_city(get_result)


def test_by_dict():
    print("\nCheck dog_list status code, fields, fields value")
    get_result: Response = Brewery.sort_breweries_by_dist()
    Assert.assert_status_code(get_result, 200)
    Assert.json_schema_by_dict(get_result)


def test_by_name():
    print("\nCheck dog_list status code, fields, fields value")
    get_result: Response = Brewery.filter_breweries_by_name()
    Assert.assert_status_code(get_result, 200)
    Assert.json_schema_by_name(get_result)


def test_by_state():
    print("\nCheck dog_list status code, fields, fields value")
    get_result: Response = Brewery.filter_breweries_by_state()
    Assert.assert_status_code(get_result, 200)
    Assert.json_schema_by_state(get_result)


def test_by_postal():
    print("\ntest_by_postal Check dog_list status code, fields, fields value")
    get_result: Response = Brewery.filter_breweries_by_postal()
    Assert.assert_status_code(get_result, 200)
    Assert.json_schema_by_postal(get_result)


def test_by_type():
    print("\ntest_by_type Check dog_list status code, fields, fields value")
    get_result: Response = Brewery.filter_breweries_by_type()
    Assert.assert_status_code(get_result, 200)
    Assert.json_schema_by_type(get_result)


def test_page():
    print("\ntest_by_type Check dog_list status code, fields, fields value")
    get_result: Response = Brewery.breweries_page()
    Assert.assert_status_code(get_result, 200)
    Assert.json_schema_page(get_result)
    Assert.range_array_3_page(get_result)


def test_per_page():
    print("\ntest_by_type Check dog_list status code, fields, fields value")
    get_result: Response = Brewery.breweries_per_page()
    Assert.assert_status_code(get_result, 200)
    Assert.json_schema_per_page(get_result)


def test_sort():
    print("\ntest_by_type Check dog_list status code, fields, fields value")
    get_result: Response = Brewery.sort_result()
    Assert.assert_status_code(get_result, 200)
    Assert.json_schema_sort(get_result)
    Assert.range_array_3_page(get_result)


def test_random_brewery():
    print("\ntest_random_brewery Check dog_list status code, fields, fields value")
    get_result: Response = Brewery.random_brewery()
    Assert.assert_status_code(get_result, 200)
    Assert.json_schema_random_brewery(get_result)


def test_size():
    '''Может фейлится из за рандома апи'''
    print("\ntest_size Check dog_list status code, fields, fields value")
    get_result: Response = Brewery.size_brewery()
    Assert.assert_status_code(get_result, 200)
    Assert.json_schema_size(get_result)


def test_search():
    print("\ntest_search Check dog_list status code, fields, fields value")
    get_result: Response = Brewery.search_breweries()
    Assert.assert_status_code(get_result, 200)
    Assert.json_schema_search(get_result)
    Assert.range_array_3_page(get_result)


def test_autocomplete():
    print("\ntest_search Check dog_list status code, fields, fields value")
    get_result: Response = Brewery.autocomplete_brewery()
    Assert.assert_status_code(get_result, 200)
    Assert.json_schema_autocomplete(get_result)
