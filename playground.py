import smtplib
import datetime as dt
import random

my_email = "jackjaggeriv@gmail.com"
my_password = "hionfetkseoeoilt"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 2:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject: Wednesday Motivation\n\n {quote}")

# import smtplib
# my_email = "jackjaggeriv@gmail.com"
# password = "hionfetkseoeoilt!!"
# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email, to_addrs="superuser@brylimz.com", msg="Subject:Hello\n\nThis is the body of my email")
# connection.close()

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1995, month=12, day=15)
# print(date_of_birth)