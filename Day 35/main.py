import requests
from array import array

import vonage as vonage

OWM_Endpoint = "http://api.openweathermap.org/data/2.5/forecast"
api_key = "33d4ca10fb3bf5061b878ce771916ac7"
api_key_sms = "NONE"
MY_LAT = 41.490678
MY_LONG = -8.674748
parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "lang": "pt",
     "cnt": 8
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()["list"]

report = list()
for data in weather_data:
    weather_description = data["weather"][0]["description"].title()

    icon_img = data["weather"][0]["icon"]
    icon_response = requests.get(f"http://openweathermap.org/img/wn/{icon_img}@2x.png")
    icon_response.raise_for_status()

    hour = data["dt_txt"].split(" ")[1].split(":")[0]
    minutes = data["dt_txt"].split(" ")[1].split(":")[1]
    time = f"{hour}H"

    day = data["dt_txt"].split(" ")[0].split("-")[-1]
    month = data["dt_txt"].split(" ")[0].split("-")[1]
    year = data["dt_txt"].split(" ")[0].split("-")[0]
    date = f"{day}/{month}"


    weather_time = f"{time}"
    report.append(f"{weather_description} {weather_time}")
str_report = ""
for data in report:
    str_report += data + "\n"
print(str_report)




###################################### SEND SMS #############################

# client = vonage.Client(key="b961a206", secret="CL1BmwuPJdSRyFzZ")
# sms = vonage.Sms(client)
#
# responseData = sms.send_message(
#     {
#         "from": "Weather Inf",
#         "to": "351967105762",
#         "text": str_report,
#     }
# )
#
# if responseData["messages"][0]["status"] == "0":
#     print("Message sent successfully.")
# else:
#     print(f"Message failed with error: {responseData['messages'][0]['error-text']}")