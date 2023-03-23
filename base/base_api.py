import json

import jsonpath as jsn
import requests


class BaseApi:

    def get_request(self, url, params=None, headers=None):
        """
        Use this method to send the get request
        :param url: The request URL
        :param params: The request Param (OPTIONAL)
        :param headers: The request headers(OPTIONAL
        :return: response
        """
        response = requests.get(url, params, headers)
        return response

    def check_status_code(self, response, expected_status_code):
        """
        Use this method to check the response status code
        :param response:
        :param expected_status_code:
        :return:
        """
        assert response.status_code == expected_status_code

    def get_json_value_by_key(self, response, key):

        json_data = json.loads(response.text)
        values_in_json = jsn.jsonpath(json_data, key)
        return values_in_json

    def get_value_from_list(self, values_list, expected_value):
        for val in values_list:
            if val == expected_value:
                return val
