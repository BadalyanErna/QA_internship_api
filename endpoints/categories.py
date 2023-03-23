from base.base_api import BaseApi


class Categories(BaseApi):

    get_category_endpoint = "api_testing/category/read.php"

    def get_categories(self, url, expected_status_code, expected_category):
        response = self.get_request(url)
        self.check_status_code(response, expected_status_code)
        list = self.get_json_value_by_key(response, '$.record..name')
        exp_value = self.get_value_from_list(list, expected_category)
