import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from config import my_mail, password


msg = MIMEMultipart('alternative')
msg['Subject'] = "Junior Python Developer"
msg['From'] = my_mail

email_list = [line.strip() for line in open('mails.csv')]
for email in email_list:
    msg['To'] = email
    html = """\
    <html>
      <head></head>
      <body>
        <p>Hi!<br>
          How are you?<br>
          Here is the <a href="http://www.python.org">link</a> you wanted.
        </p>
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

    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login(my_mail, password)
    mail.sendmail(my_mail, email, msg.as_string())
    mail.quit()
