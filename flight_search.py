import requests
from datetime import datetime
from dateutil.relativedelta import relativedelta
from flight_data import FlightData


class FlightSearch:
    def __init__(self, data):
        self.data = data
        self.flight_search_endpoint = 'https://tequila-api.kiwi.com'
        self.API_KEY = "zWEDT49EhU9Wdr4zoTAC6ZwfeqXXSGAw"
        self.today = datetime.now().strftime("%d/%m/%Y")
        self.matching_flights_endpoint = 'http://tequila-api.kiwi.com/v2/search'
        self.headers = {
            "apikey": self.API_KEY,
        }
        self.stop_overs = 0

    def iata_code(self):
        headers = {
            "apikey": self.API_KEY
        }
        for data in self.data:
            api_end_point = f"{self.flight_search_endpoint}/locations/query"
            query = {
                "term": data['city'],
                "location_types": "city"
            }
            response = requests.get(url=api_end_point, params=query, headers=headers)
            new_data = response.json()['locations'][0]
            data['iataCode'] = new_data['code']

        return self.data

    def search_flight(self, departure_city, least_price):
        six_months = (datetime.today() + relativedelta(months=+6)).strftime("%d/%m/%Y")
        params = {
            "fly_from": "LON",
            "fly_to": departure_city,
            "date_from": self.today,
            "data_to": six_months,
            "curr": "GBP",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
        }
        response = requests.get(url=self.matching_flights_endpoint, params=params, headers=self.headers)
        print(response.status_code)
        try:
            data = response.json()['data'][0]
        except IndexError:
            params['max_stopovers'] = 1
            response = requests.get(url=self.matching_flights_endpoint, params=params, headers=self.headers)
            print(response.status_code)
            try:
                data = response.json()['data'][0]
                self.stop_overs = 1
            except IndexError:
                return print(f"No flights available to {departure_city}")
        if self.stop_overs == 1:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][self.stop_overs]["cityTo"],
                destination_airport=data["route"][self.stop_overs]["flyTo"],
                via_city=data['route'][self.stop_overs]['cityFrom'],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0],
                stop_overs=1
            )
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][self.stop_overs]["cityTo"],
                destination_airport=data["route"][self.stop_overs]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data
