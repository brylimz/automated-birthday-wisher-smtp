import smtplib
my_email = "brylimz@gmail.com"
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()