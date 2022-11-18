# import smtplib
#
# my_email = "None"
# password = "None"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs=my_email,
#         msg="Subject:Hello\n\nThis is the body of my email!")


import datetime as dt
now = dt.datetime.now().day
print(now)

date_of_birth = dt.datetime(year=1993, month=6, day=17)
print(date_of_birth)