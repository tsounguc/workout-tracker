from datetime import datetime, timedelta

import requests

APP_ID = ""
API_KEY = ""

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

parameters = {
 "query": input("Tell me which exercises you did: "),
 "gender": "male",
 "weight_kg": 72.5,
 "height_cm": 175.26,
 "age": 27
}

respond = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
respond.raise_for_status()
data = respond.json()

print(data)

sheety_endpoint = "https://api.sheety.co/0d6888b4ea372773b01f568e0d405d57/workoutTracking/workouts"

exercises = data['exercises']
today = datetime.now()

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

    respond = requests.post(url=sheety_endpoint, json=sheety_parameters)
    print(respond.json())
