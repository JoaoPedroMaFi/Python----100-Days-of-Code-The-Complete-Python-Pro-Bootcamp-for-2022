import datetime
import os
import requests


GENDER = "Male"
WEIGHT_KG = 80
HEIGHT_CM = 175
AGE = 25

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
print(API_KEY)
print(APP_ID)


headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

exercise_text = input("Tell me which exercises you did: ")

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
exercise_endpoint = " https://trackapi.nutritionix.com/v2/natural/exercise"



response = requests.post(url=exercise_endpoint, headers=headers, json=parameters)
result = response.json()
print(result)

################### Start of Step 4 Solution ######################

sheets_endpoint = os.environ["SHEET_ENDPOINT"]

bearer_headers = {
    "Authorization": f"Bearer {os.environ['TOKEN']}" #fnfjpotgk+rgk,re+poge+rpyihep+rlhep+rerthp´sthrtºheçr,ergm,ertm"
    }

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": datetime.datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.datetime.now().strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=sheets_endpoint, json=sheet_inputs, headers=bearer_headers)
    print(sheet_response.json())

# https://api.sheety.co/12a2a4afc188a9c1c513e1fcb31d6b3e/workoutTracking/workouts

# run 2 miles and walked 3km