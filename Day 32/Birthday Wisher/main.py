import random
import smtplib
import datetime as dt

now = dt.datetime.now()
weekday = now.weekday()

my_email = "jpmf19930617@gmail.com"
password = "shlwjibaqbctjhbe"

if weekday == 0:
    with open("quotes.txt") as data_file:
        all_quotes = data_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Monday Motivation\n\n{quote}")

