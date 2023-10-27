# Stock Trading Alert
Queries stock trading API to check for company's closing share prices in the previous 2 days. Sends an SMS via Twilio's SMS API to user's phone number(s) before market opens in case share price has dipped below a threshold percentage in the last 2 days with share information and latest news articles for that company.

I used [AlphaVantage API](https://www.alphavantage.co/) for company share prices and [NewsAPI](https://newsapi.org/) to extract the news articles for the company.

## Prerequisites:
- Create an account in [AlphaVantage API](https://www.alphavantage.co/) & [NewsAPI](https://newsapi.org/) and generate your API keys.
- Create an account in [Twilio](https://www.twilio.com/en-us), generate your Twilio phone number, verify your personal number(s) and set aside your Twilio Auth Token and Account SID.
- Create environment variables containing your private API keys and tokens within your local environment by typing in terminal:
  
  ```bash
   export ALPHAVANTAGE_API_KEY=alphavantage_api_key
   export NEWS_API_KEY=news_api_key
   export TWILIO_AUTH_TOKEN=twilio_api_key
  ```
  
- Python 3.9 & up

### To run in terminal:
- Open Powershell in the local repository folder
- Type:

  ```bash
   python main.py
  ```
### Expected Output
I ran the program for Tesla Inc. with a threshold % difference of 2% (rise/dip) in price. The closing share price values for the `TSLA` stock in the last 2 days were `$205.76` and `$212.42` having a `3.23678 %` difference. I received SMSes on my phone as below:

```bash
Sent from your Twilio trial account - Tesla: 🔻3%
Headline: The DOJ Tesla probe has expanded to include EV driving ranges. 
Brief: The Department of Justice has expanded its investigation into Tesla, the company has confirmed. In an SEC filing, Tesla said the agency has issued subpoenas for information related to "personal benefits, related parties, vehicle range and personnel decisi…"

Sent from your Twilio trial account - Tesla: 🔻3%
Headline: Tesla profits dip as it invests in factory upgrades and AI development. 
Brief: Tesla reported its Q3 earnings for 2023 in which the company’s revenues dipped compared to the previous quarter thanks to planned factory shutdowns.

Sent from your Twilio trial account - Tesla: 🔻3%
Headline: Tesla’s first Cybertruck deliveries will happen on November 30th. 
Brief: Tesla will deliver the first units of its electric pickup truck Cybertruck on November 30th after missing multiple previous deadlines. The pickup truck was originally announced in 2019.
```

This program can be automated to run daily before stock market open times to notify users of details with stocks they are interested in in order to plan ahead.
