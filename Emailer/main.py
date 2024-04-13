import datetime as dt
import random
import smtplib
import pandas as pd
import environ 

env = environ.Env()

environ.Env.read_env()

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
date_of_birth = dt.datetime(year=1998, month=7, day=27)

my_email = env('MYEMAIL')
password = env('EMAIL_PASSWORD')

if 5 == day_of_week:
    with open("Emailer/quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    
    with smtplib.SMTP("smtp-mail.outlook.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=env("TOEMAIL"),
            msg=f"Subject:this is my quote that was random asf\n\n{quote}"
        )





with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
    connection.starttls()
print(day_of_week)
print("hello") 