import requests
import math
import os
from datetime import datetime, timedelta
from twilio.rest import Client

# TWILIO account details
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

# Company Info
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla"

# API Base URLS
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# Secret API keys
ALPHA_API_KEY = os.environ["ALPHAVANTAGE_API_KEY"]
NEWS_API_KEY = os.environ["NEWS_API_KEY"]


# Function to send SMS via Twilio
def send_news(msg, symbol):
    for article in msg:
        message = client.messages \
            .create(
            body=f"{COMPANY_NAME}: {symbol}{math.floor(percent_difference)}%\n{article}",
            from_='TWILIO_PHONE_NUMBER',
            to='VERIFIED_PHONE_NUMBER')


symbol = None

# Storing dates of day before and day before yesterday
yesterday = str(datetime.today() - timedelta(days=1)).split(" ")[0]
day_before_yesterday = str(datetime.today() - timedelta(days=2)).split(" ")[0]

# Querying the Trading API and parsing the json data for closing price data of the company's stock for both days
url = f'{STOCK_ENDPOINT}?function=TIME_SERIES_DAILY&symbol={STOCK_NAME}&outputsize=compact&apikey={ALPHA_API_KEY}'
r = requests.get(url)
data = r.json()

yesterday_closing = float(data["Time Series (Daily)"][yesterday]['4. close'])
day_before_yesterday_closing = float(data["Time Series (Daily)"][day_before_yesterday]['4. close'])

closing_difference = yesterday_closing - day_before_yesterday_closing
percent_difference = abs(closing_difference)/yesterday_closing * 100

if closing_difference > 0:
    symbol = "🔺"
else:
    symbol = "🔻"

# Extracting last 3 news articles related to the company via the NEWS API
url = f'https://newsapi.org/v2/everything?q={COMPANY_NAME}&apiKey={NEWS_API_KEY}'
r = requests.get(url)
info = data["articles"][:3]

# Creating a list containing title and description of the last 3 news articles
msg = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in info]

# Send an SMS to user if the % difference of closing prices is below threshold amount
if percent_difference > 3:
    send_news(msg, symbol)
