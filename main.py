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
 "query": "ran 3 miles",
 "gender": "male",
 "weight_kg": 72.5,
 "height_cm": 175.26,
 "age": 27
}

respond = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
respond.raise_for_status()
data = respond.json()

print(data)
