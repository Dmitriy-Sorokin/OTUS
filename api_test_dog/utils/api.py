from api_test_dog.utils.dog_http_methods import Http_methods

''' Methods for tests Google_maps_api'''

base_url = "https://dog.ceo"


class Dog_api():
    '''Methods dog list'''

    @staticmethod
    def dog_list():
        get_resource = "/api/breed/hound/list"  # Resource method get
        get_url = base_url + get_resource
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.json())
        return result_get

    @staticmethod
    def dog_images():
        get_resource = "/api/breed/hound/afghan/images"
        get_url = base_url + get_resource
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.json())
        return result_get

    @staticmethod
    def dog_random():
        get_resource = "/api/breed/hound/afghan/images/random/1"
        get_url = base_url + get_resource
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.json())
        return result_get
