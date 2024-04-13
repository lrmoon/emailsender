import datetime as dt
import random
import smtplib

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
date_of_birth = dt.datetime(year=1998, month=7, day=27)

my_email = "brownjoel83@yahoo.com"
password = "fvvjjvpfuyinjncl"

if 6 == day_of_week:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="johnnydoe0607@gmail.com",
            msg=f"Subject:Quote of the day\n\n{quote}"
        )





with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
    connection.starttls()

print("hello") 