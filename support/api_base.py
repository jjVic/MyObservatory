import requests
import json

class APIBase(object):
    def get_response_data(self, request_method, url):
        response = requests.request(request_method, url)
        return response.text

    def get_response_status_code(self, request_method, url):
        response = requests.request(request_method, url)
        return response.status_code

    def load_data_in_json(self, response_text):
        return json.loads(response_text)
