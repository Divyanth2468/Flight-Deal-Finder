from notification_manager import NotificationManager
from data_manager import DataManager
from flight_search import FlightSearch
data = DataManager()
sheet_data = data.get_data()
flight_search = FlightSearch(sheet_data)
sms = NotificationManager()

if sheet_data[0]['iataCode'] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.iata_code()
    data.destination_data = sheet_data
    data.put_destination_code_data()

users_data = data.get_user_data()
emails = []
for data in users_data['users']:
    print(data)
    email = data['email']
    print(email)
    emails.append(email)

for data in sheet_data:
    available_flight_data = flight_search.search_flight(departure_city=data['iataCode'], least_price=data['lowestPrice'])
    if available_flight_data == None:
        pass
    elif available_flight_data.price <= data['lowestPrice']:
        link = f"https://www.google.co.uk/flights?hl=en#flt={available_flight_data.origin_airport}" \
               f".{available_flight_data.destination_airport}.{available_flight_data.out_date}*" \
               f"{available_flight_data.destination_airport}.{available_flight_data.origin_airport}." \
               f"{available_flight_data.return_date}"
        if available_flight_data.via_city != "":
            sms.send_email(
                link=link,
                emails=emails,
                message=f"Low price alert! Only £{available_flight_data.price} to fly from "
                        f"{available_flight_data.origin_city}-{available_flight_data.origin_airport} to "
                        f"{available_flight_data.destination_city}-{available_flight_data.destination_airport}, from "
                        f"{available_flight_data.out_date} to {available_flight_data.return_date}.\n"
                        f"Flight has 1 stop over,via {available_flight_data.via_city} City."
            )
        else:
            sms.send_email(
                link=link,
                emails=emails,
                message=f"Low price alert! Only £{available_flight_data.price} to "
                        f"fly from {available_flight_data.origin_city}-{available_flight_data.origin_airport} to "
                        f"{available_flight_data.destination_city}-{available_flight_data.destination_airport}, from "
                        f"{available_flight_data.out_date} to {available_flight_data.return_date}."
            )



