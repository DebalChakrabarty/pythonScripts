import smtplib

host = "smtp.gmail.com"
port = 587
username="ratulchakrabarty1994@gmail.com"
password="Counter1234!"

from_email=username
to_list=["debalchakrabarty@gmail.com"]

email_con=smtplib.SMTP(host,port)

email_con.ehlo()

email_con.starttls()

email_con.login(username,password)

email_con.sendmail(from_email,to_list,"hey there")
