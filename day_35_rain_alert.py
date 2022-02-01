#  this code will work on pythonanywhere
import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {'https': os.environ['https_proxy']}

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

# OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
# api_key = "30585603999f2d94b0306b75ad0fe5b2"
# My_lat = 26.206300
# My_long = 83.970600
# parameters = {
#     "lat": My_lat,
#     "lng": My_long,
#     "appid":api_key,

# }
account_sid = 'AC269aa9e8b92ade105cb6dbee707ad96c'
auth_token = '5b89e19878fab7b52aececfd89517f9c'
client = Client(account_sid, auth_token, http_client=proxy_client)
response  = requests.get(url="https://api.openweathermap.org/data/2.5/onecall?lat=26.206300&"
                             "lon=83.970600&"
                             "appid=30585603999f2d94b0306b75ad0fe5b2")
weather_data = response.json()

id_list = []
# condition = []
id = weather_data["daily"][0]["weather"][0]["id"]
# cond = weather_data["daily"][i]["weather"][0]["main"]
id_list.append(id)
# condition.append(cond)
if(id<300):
    message = client.messages.create(
        body="tunderstorm hoga bhai aaj",
        from_='+17127982620',
        to='+919829895619'
    )

    print(message.sid)
elif(id<400):
    message = client.messages.create(
        body="drizle hai bhai aaj",
        from_='+17127982620',
        to='+919829895619'
    )

    print(message.sid)
elif (id < 600):
    message = client.messages.create(
        body="barish hoga bhai aaj ",
        from_='+17127982620',
        to='+919829895619'
    )

    print(message.sid)
else:
    message = client.messages.create(
        body="clear hai aaj weather",
        from_='+17127982620',
        to='+919829895619'
    )

    print(message.sid)
