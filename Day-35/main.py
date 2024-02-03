import os
from dotenv import load_dotenv
import requests
from twilio.rest import Client

load_dotenv()

API_key = os.getenv("OPENWEATHER_KEY")
lat = os.getenv("MY_LAT")
long = os.getenv("MY_LONG")
weather_params = {
    "lat" : lat,
    "lon": long,
    "appid" : API_key,
    "cnt": 4

}
response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast", params=weather_params)
weather_data = response.json()

is_rain = False
hourly_list = weather_data['list']

for data in hourly_list:
    inside_list =  data['weather']
    for inner_data in inside_list:
        if int(inner_data['id']) < 700 :
            is_rain = True


account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

if is_rain:
    message = "Sir Please take umbrella today, weather is not good and dont forget to get momos back at home !"
else:
    message = "No need for umbrella today, Have a great day Sir."
sms = client.messages \
                .create(
                    body=message,
                    from_=os.getenv('TWILIO_GENERATED_NUMBER'),
                    to=os.getenv('MY_NUMBER')
                )

print(sms.body)

