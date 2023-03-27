import requests
from datetime import datetime
import time
import smtplib

MY_EMAIL = "#####@gmail.com"
MY_PASSWORD = "@@@@@"
MY_LAT = 28.704060
MY_LONG = 77.102493


def iss_overhead():
    parameters = {
        'lat': MY_LAT,
        'lng': MY_LONG,
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    iss_lat = float(data["iss_position"]["latitude"])
    iss_long = float(data["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_lat <= MY_LAT +5 and MY_LONG-5 <= iss_long <= MY_LONG+5:
        return True


def is_night():
    parameters = {
        'lat': MY_LAT,
        'lng': MY_LONG,
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now >= sunset and time_now<=sunrise:
        return True

while True:
    time.sleep(60)

    if is_night() and iss_overhead():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
                            msg="Subject : LOOK UP \n\n ISS is overhead")
