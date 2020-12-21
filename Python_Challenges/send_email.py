import smtplib
import email.mime.text
import time
import random
def send_email(to,subject,body):

    for i in range(0,100):
        gmail_user='your@gmail.com'
        gmail_password='@password'
        sent_from = 'your@gmail.com'
        to = to
        subject = subject
        body =body

        email_text =email.mime.text.MIMEText("""\
        From: %s
        To: %s
        Subject: %s

        %s
        """ % (sent_from, to, subject, body), _charset="UTF-8")
        server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server_ssl.ehlo()
        print("Helo Successful") # optional
        server_ssl.login(gmail_user, gmail_password)
        print("Login Successful")
        server_ssl.sendmail(sent_from, to, email_text.as_string())
        server_ssl.close()
        sleep_val=random.randint(300,550)
        time.sleep(sleep_val)

to=input("Give receive adress :")
subject=input("Give Subject :")
body=input("Write text here :")
send_email(to,subject,body)
