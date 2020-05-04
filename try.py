import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from config import my_mail, password


msg = MIMEMultipart('alternative')
msg['Subject'] = "Junior Python Developer"
msg['From'] = my_mail

email_list = [line.strip() for line in open('mails-1.csv')]

html = """\
<html>
  <body>
    <p>To Whom It May Concern,</p>
    <p>My name is Sergii Shevchenko and I am writing to you to enquire about any possible up and coming openings or opportunities with your company.</p>
    <p>I have one-year of experience and I am looking for new opportunities as a Junior Python Developer.</p>
    <p>For your convenience, my enclosed resume contains the details about my qualifications, experience, and skills.</p>
    <p>In addition, you can find the link to my GitHub account here - https://github.com/sergiishevchenko.</p>
    <p>I am really interested in working for your company (including voluntary or work experience opportunities).</p>
    <p>I am fully prepared to commit to any training that might be required.</p>
    <p>Should you have any questions or require any further information, please do not hesitate to contact me.</p>
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
# permission = MIMEApplication(open("Job permission.pdf", "rb").read())
# permission.add_header('Content-Disposition', 'attachment', filename="Job permission.pdf")
# msg.attach(permission)

# Attach Resume to the email
cv = MIMEApplication(open("sergii-shevchenko.cv.pdf", "rb").read())
cv.add_header('Content-Disposition', 'attachment', filename="sergii-shevchenko.cv.pdf")
msg.attach(cv)

# Attach Legitimation card to the email
# card = MIMEApplication(open("sergii-shevchenko.legitimation-card R.pdf", "rb").read())
# card.add_header('Content-Disposition', 'attachment', filename="sergii-shevchenko.legitimation-card R.pdf")
# msg.attach(card)

for email in email_list:
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login(my_mail, password)
    mail.sendmail(my_mail, email, msg.as_string())
    mail.quit()
