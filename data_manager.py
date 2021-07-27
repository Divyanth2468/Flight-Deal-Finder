import requests


class DataManager:
    def __init__(self):
        self.endpoint = 'https://api.sheety.co/472cf5c878778bec1e64deb2aaa4ede2/flightSearch/sheet1'
        self.users_endpoint = 'https://api.sheety.co/472cf5c878778bec1e64deb2aaa4ede2/flightSearch/users'
        self.APP_ID = 'df40ca29'
        self.API_KEY = '472cf5c878778bec1e64deb2aaa4ede2'
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