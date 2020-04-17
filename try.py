import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from config import my_mail, password


msg = MIMEMultipart('alternative')
msg['Subject'] = "Junior Python Developer"
msg['From'] = my_mail

email_list = [line.strip() for line in open('mails.csv')]

html = """\
<html>
  <body>
    <p>To Whom It May Concern,</p>
    <p>My name is Sergii Shevchenko and I am a Python Web Developer with an experience of 1 year.</p>
    <p>Currently, I am looking for new opportunities as a Junior Python Developer.</p>
    <p>I live in Lausanne, canton of Vaud.</p>
    <p>I have permission to live and work in Switzerland (Legitimation card R, Permission Ci).</p>
    <p>Unfortunately, I don't speak French and German (only English and Russian).</p>
    <p>My GitHub account - https://github.com/sergiishevchenko</p>
    <p>Should you require further information, please do not hesitate to contack me.</p>
    <p>Attached you can find the documents that may interest you.</p>
    <p></p>
    <p></p>
    <p></p>
    <p>Best regards</p>
    <p>Sergii Shevchenko</p>
    mail: sergsheva1704@gmail.com<br>
    telegram: @sergsheva<br>
    tel.: +41778154379
  </body>
</html>
"""
attachment = MIMEText(html, 'html')
msg.attach(attachment)

# Attach Job permission to the email
permission = MIMEApplication(open("Job permission.pdf", "rb").read())
permission.add_header('Content-Disposition', 'attachment', filename="Job permission.pdf")
msg.attach(permission)

# Attach Resume to the email
cv = MIMEApplication(open("sergii-shevchenko.cv.pdf", "rb").read())
cv.add_header('Content-Disposition', 'attachment', filename="sergii-shevchenko.cv.pdf")
msg.attach(cv)

# Attach Legitimation card to the email
card = MIMEApplication(open("sergii-shevchenko.legitimation-card R.pdf", "rb").read())
card.add_header('Content-Disposition', 'attachment', filename="sergii-shevchenko.legitimation-card R.pdf")
msg.attach(card)

for email in email_list:
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login(my_mail, password)
    mail.sendmail(my_mail, email, msg.as_string())
    mail.quit()
