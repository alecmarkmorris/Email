import smtplib
from email.message import EmailMessage
import ssl

# Enter your email Address here
EMAIL_ADDR = "alecmarkmorris@gmail.com"

#Enter you password given by Google
EMAIL_PASS = "sgsmbcxhycvjojjm"

#Enter the receiver
EMAIL_REC = "4802996741@vtext.com"


def send_email(subject, body, to):
    msg= EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = "alecmarkmorris@gmail.com"
    msg['from'] = user
    password = "sgsmbcxhycvjojjm"  

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    print("Message sent")

    server.quit()


send_email("Test Subject", "Test Body", "4802996741@vtext.com")

