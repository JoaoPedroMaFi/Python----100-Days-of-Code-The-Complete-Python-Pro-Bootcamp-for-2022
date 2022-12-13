import requests

SHEETY_ENDPOINT = "https://api.sheety.co/12a2a4afc188a9c1c513e1fcb31d6b3e/flightDeals/prices"


class DataManager:

    def __init__(self):
        self.destination_data = []

    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        self.destination_data = response.json()["prices"]
        return response.json()["prices"]

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)