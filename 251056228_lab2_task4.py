import smtplib
from email.mime.text import MIMEText

YOUR_EMAIL = input("Enter your email address: ")
YOUR_PASSWORD = input("Enter your password: ")
YOUR_DESTINATION_EMAIL = input("Enter email destination: ")

msg = "I love computer networks! this is my task 4 message"

# Choose a mail server
mailserver = 'smtp.gmail.com'

# Create an SMTP object and connect to the mail server
smtp = smtplib.SMTP(mailserver, 587)
smtp.starttls()

# Login to email account
smtp.login(YOUR_EMAIL, YOUR_PASSWORD)

# Compose the email message
message = MIMEText(msg)
message['From'] = YOUR_EMAIL
message['To'] = YOUR_DESTINATION_EMAIL
message['Subject'] = "Test Email Subject"

# Send the email
smtp.sendmail(YOUR_EMAIL, YOUR_DESTINATION_EMAIL, message.as_string())

smtp.quit()
