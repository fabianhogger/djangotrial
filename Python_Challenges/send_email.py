import smtplib
def send_email(to,subject,body):
    gmail_user='draizfabian@gmail.com'
    gmail_password='RandomWords.com'
    sent_from = 'draizfabian@gmail.com'
    to = [to]
    subject = subject
    body = body

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server_ssl.ehlo()
    print("Helo Successful") # optional
    server_ssl.login(gmail_user, gmail_password)
    print("Login Successful")
    server_ssl.sendmail(sent_from, to, email_text)
    server_ssl.close()

to=input("Give receive adress :")
subject=input("Give Subject :")
body=input("Write text here :")
print(type(to),type(subject),type(body  ))
send_email(to,subject,body)
"""
import smtplib
def send_mail(to,subject,body):
    gmail_user='draizfabian@gmail.com'
    gmail_password='adasd'
    sent_from = 'draizfabian@gmail.com'
    to = to
    subject = subject
    body = body


    server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server_ssl.ehlo()
    print("Helo Successful") # optional
    server_ssl.login(gmail_user, gmail_password)
    print("Login Successful")
    server_ssl.sendmail(sent_from, to, email_text)
    server_ssl.close()


to=input("Give receive adress :")
subject=input("Give Subject :")
body=input("Write text here :")
send_mail(to,subject,body)

"""
