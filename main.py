import smtplib
my_email = "jackjaggeriv@gmail.com"
password = "hionfetkseoeoilt"
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="superuser@brylimz.com", msg="Hello")
connection.close()

