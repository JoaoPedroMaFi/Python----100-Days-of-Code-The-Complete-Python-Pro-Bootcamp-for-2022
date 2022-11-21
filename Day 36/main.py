import smtplib
import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "VV6P45XEPSLEHBK7"
NEWS_API_KEY = "be0704791345478983e52462608f8738"

# STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY

}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
last_day = data_list[0]
last_day_closing_price = last_day["4. close"]
print(last_day_closing_price)

# Get the day before yesterday's closing stock price
day_before_last_day = data_list[1]
day_before_last_day_closing_price = day_before_last_day["4. close"]
print(day_before_last_day_closing_price)

# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = float(last_day_closing_price) - float(day_before_last_day_closing_price)
print(difference)
up_down = None
if difference > 0:
    up_down = "UP "
    # "🔺".encode()
else:
    up_down = "DOWN "
    # "🔻".encode()
difference = abs(difference)
print(u'\U0001f53a')
# Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = round((difference / float(last_day_closing_price)) * 100)
print(diff_percent)
# TIf TODO4 percentage is greater than 5 then print("Get News").
# Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

if diff_percent > 1:
    news_params = {
        "apikey": NEWS_API_KEY,
        "q": COMPANY_NAME,
        "searchIn": "title"
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    # STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

    # Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles = articles[:3]

    # STEP 3: Use twilio.com/docs/sms/quickstart/python
    # to send a separate message with each article's title and description to your phone number.

    # Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_articles = [
        f"{STOCK_NAME}: {up_down}{diff_percent}%\n\nHeadline: {article['title']}.\n\nBrief: {article['description']}"
        for article in three_articles]
    print(formatted_articles)
    # Send email each article as a separate message via Twilio.

    my_email = "NONE"
    password = "NONE"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        for article in formatted_articles:
            connection.sendmail(from_addr=my_email,
                                to_addrs=my_email,
                                msg=f"Subject:Important News\n\n{article}")

# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
