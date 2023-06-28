# Import relevant libraries to make HTTP requests and parse JSON response
import requests
import json


class AskOpenTargets:
    def __init__(self, base_url):
        self.base_url = base_url

    def search(self, query_string):
        try:
            api_response = requests.post(self.base_url, json={"query": query_string})
            api_response.raise_for_status()
            api_response = json.loads(api_response.text)
            return api_response
        except requests.exceptions.HTTPError as err:
            print(err)

