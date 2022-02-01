import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {'https': os.environ['https_proxy']}
account_sid = 'AC269aa9e8b92ade105cb6dbee707ad96c'
auth_token = '5b89e19878fab7b52aececfd89517f9c'
client = Client(account_sid, auth_token, http_client=proxy_client)
api_key = "9TYM1HNSATM5FV3F"
news_api_key = "570ef4ae579744438fe5bf0664650db8"
stock_endpoint = "https://www.alphavantage.co/query"
news_endpoint = "https://newsapi.org/v2/everything"
crypto_name = "DOGE"
crypto_market = "INR"
crypto_paras = {
    "function": "DIGITAL_CURRENCY_DAILY",
    "symbol": crypto_name,
    "market": crypto_market,
    "apikey": api_key
}

response = requests.get(url=stock_endpoint, params=crypto_paras)
data = response.json()
data_time_series = data["Time Series (Digital Currency Daily)"]
date_list = [value for (key, value) in data_time_series.items()]
yesterday_open_inr = date_list[1]['1a. open (INR)']
yesterday_close_inr = date_list[1]['4a. close (INR)']
yesterday_low_inr = date_list[1]['3a. low (INR)']
yesterday_high_inr = date_list[1]['2a. high (INR)']
day_before_yesterday_open_inr = date_list[2]['1a. open (INR)']
day_before_yesterday_close_inr = date_list[2]['4a. close (INR)']
diff = (float(day_before_yesterday_close_inr) - float(yesterday_close_inr))
diff_percentage = (diff / float(yesterday_close_inr)) * 100
if diff_percentage > 0:
    news_paras = {
        "q": crypto_name,
        "apiKey": news_api_key
    }
    res = requests.get(news_endpoint, params=news_paras)
    news_data = res.json()["articles"]
    three_articles = news_data[0]
    msg =f"\n{crypto_name} 🔼 {diff_percentage}% \n Current Price:{date_list[0]['1a. open (INR)']}\nHeadline : {three_articles['title']}.\nBrief: {three_articles['description']}"
    # print(three_articles)
    message = client.messages.create(
        body=msg,
        from_='+17127982620',
        to='+919829895619'
    )

    print(message.sid)
else:
    news_paras = {
        "q": crypto_name,
        "apiKey": news_api_key
    }
    res = requests.get(news_endpoint, params=news_paras)
    news_data = res.json()["articles"]
    three_articles = news_data[0]
    msg = f"\n{crypto_name} 🔽{diff_percentage}% \n Current Price:{date_list[0]['1a. open (INR)']}\nHeadline : {three_articles['title']}.\nBrief: {three_articles['description']}"
    # print(three_articles)
    message = client.messages.create(
        body=msg,
        from_='+17127982620',
        to='+919829895619'
    )

    print(message.sid)
#     print(news_list)
#     # print(news_data)
# print(yesterday_high_inr)
# print(yesterday_close_inr)
# print(yesterday_open_inr)
# print(yesterday_low_inr)
# print(diff_percentage)
