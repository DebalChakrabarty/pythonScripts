import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

host = "smtp.gmail.com"
port = 587
username="ratulchakrabarty1994@gmail.com"
password="Counter1234!"
from_email=username
to_list=["debalchakrabarty@gmail.com"]
try:
    email_con=smtplib.SMTP(host,port)
    email_con.ehlo()
    email_con.starttls()
    email_con.login(username,password)
    
    the_msg= MIMEMultipart("alternative")
    the_msg['Subject']="Hello There!"
    the_msg["From"]=from_email
    #the_msg["To"]=to_list
    
    plain_text="Testing the message"
    html_txt = """\
    <html>
        <head></head>
        <body> 
            <p>Hey! <br>
                Testing this email <b> message </b>. Made by <a href='http://joincfe.com'> Team CFE </a>
            </p>
        </body>
    </html>
    """
            
    part_1=MIMEText(plain_text,'plain')
    part_2=MIMEText(html_txt,"html")
    
    the_msg.attach(part_1)
    the_msg.attach(part_2)
    
    
    email_con.sendmail(from_email,to_list,the_msg.as_string())
    email_con.quit() #to quit
except smtplib.SMTPException:
    print("error sending message")
