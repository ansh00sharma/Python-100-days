import json
import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers_1 = {
    "x-app-id": os.getenv("NUTRITIONIX_APP_ID"),
    "x-app-key" : os.getenv("NUTRITIONIX_API_KEY")
}

test = input("Tell us about your workout : ")
body_params = {
    "query": test
}
response_1 = requests.post(nutritionix_endpoint, json=body_params, headers=headers_1)
response_1 = response_1.json()
# print(response_1["exercises"][0])

timestamp = datetime.now()

shetty_params = {
    "workout": {
    "date" : timestamp.strftime("%d/%m/%Y"),
    "time": timestamp.strftime("%X"),
    "exercise": response_1["exercises"][0]['user_input'],
    "duration":response_1["exercises"][0]['duration_min'],
    "calories" : response_1["exercises"][0]['nf_calories']
    }
}
headers_2 = { 
    "Authorization": f"Bearer {os.getenv('SHETTY_BEARER_TOKEN')}",
    "Content-Type": "application/json"
}
print(shetty_params)
shetty_post_endpoint = "https://api.sheety.co/a42e58097d3bfe43de0422a8dadf5f5a/ansh/workouts"
response_2 = requests.post(shetty_post_endpoint, json=shetty_params, headers=headers_2)
print(response_2.json())

