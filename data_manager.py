import requests
import os

class DataManager:
    def __init__(self):
        self.endpoint = os.getenv("end_point")
        self.users_endpoint = os.getenv("users_end_point")
        self.APP_ID = os.getenv("APP_ID")
        self.API_KEY = os.getenv("SPI_KEY")
        self.headers = {
            "Content-Type": "application/json"
        }

    def get_data(self):
        response = requests.get(url=self.endpoint)
        data = response.json()
        return data['sheet1']

    def put_destination_code_data(self):
        for city in self.get_data():
            put_endpoint = f"{self.endpoint}/{city['id']}"
            params = {
                'sheet1': {
                    "iataCode": city['iataCode']
                }
            }
            response = requests.put(url=put_endpoint, json=params, headers=self.headers)
            print(response.status_code)

    def get_user_data(self):
        response = requests.get(url=self.users_endpoint)
        data = response.json()
        return data
