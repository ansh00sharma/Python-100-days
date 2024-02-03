import requests
import os
from dotenv import load_dotenv

load_dotenv()

stock_params = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : "IBM",
    "apikey": os.getenv("APLHAVANTAGE_API_KEY")
}
stock_response = requests.get("https://www.alphavantage.co/query", params=stock_params)
stock_response = stock_response.json()['Time Series (Daily)']
yesterday_data_closing_price = stock_response['2024-02-02']['4. close']
day_before_yesterday_data_closing_price = stock_response['2024-02-01']['4. close']

# print(yesterday_data_closing_price, day_before_yesterday_data_closing_price)

difference = float(yesterday_data_closing_price) - float(day_before_yesterday_data_closing_price)
if difference > 0 :
    status = "⏫"
else:
    status = "⏬"

percent_difference = abs(difference)/float(yesterday_data_closing_price) * 100
stock_name = "IBM"
news_params = {
    "q": f"{stock_name}",
    "apiKey":os.getenv("NEWS_API_API_KEY")
}
news_response = requests.get("https://newsapi.org/v2/everything",params=news_params)
news_response = news_response.json()
# print("response : ", news_response.json())

news_articles = news_response['articles'][:5]


formatted_articles = [f"{stock_name}{status} News : {news['title']}, Detail : {news['description']}." for news in news_articles]

for item in formatted_articles:
    print(item)