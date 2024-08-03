import requests
from twilio.rest import Client
import os

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("TWILIO_SID")
auth_token = os.environ.get("TWILIO_AUTH")
twilio_phone = os.environ.get("TWILIO_PHONE")
my_phone = os.environ.get("MY_PHONE")
weather_params = {
    "lat" : 1.352083,
    "lon" : 103.819839,
    "appid" : api_key,
    "cnt": 4,
}

will_rain = False
resp = requests.get(OWM_Endpoint, params=weather_params)
resp.raise_for_status()
weather_data = resp.json()

# print(weather_data["list"][0]["weather"][0]["id"])
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code ) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
            body="Bring an umbrella ☔",
            from_=twilio_phone,
            to=my_phone,
    )
    print(message.status)
