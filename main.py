from datetime import datetime, timedelta
import os
import requests

# APP_ID = os.environ["APP_ID"] – raises exception if key does not exist
# APP_ID = os.environ.get("APP_ID") – returns None if key does not exist
# APP_ID = os.environ.get("APP_ID", “Message”) – returns “Message” if key does not exist
APP_ID = os.environ.get("APP_ID", "Message")
API_KEY = os.environ.get("API_KEY", "Message")
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT", "Message")
TOKEN = os.environ.get("TOKEN", "Message")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

exercise_parameters = {
    "query": input("Tell me which exercises you did: "),
    "gender": "male",
    "weight_kg": 72.5,
    "height_cm": 175.26,
    "age": 27
}

exercise_respond = requests.post(url=exercise_endpoint, json=exercise_parameters, headers=exercise_headers)
exercise_respond.raise_for_status()
data = exercise_respond.json()
exercises = data['exercises']
today = datetime.now()

print(data)

sheety_headers = {
    "Authorization": f"Bearer {TOKEN}"
}

for exercise in exercises:
    sheety_parameters = {
        "workout": {
            "date": today.strftime("%Y/%m/%d"),
            "time": today.strftime("%H:%m:%S"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheety_respond = requests.post(url=SHEETY_ENDPOINT, json=sheety_parameters, headers=sheety_headers)
    print(sheety_respond.json())
