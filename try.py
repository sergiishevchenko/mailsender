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
    # msg['To'] = email
    html = """\
    <html>
      <body>
        <p>To Whom It May Concern,</p>
        <p>My name is <strong>Sergii Shevchenko</strong> and I am a <strong>Python Web Developer</strong> with an experience of <strong style="color:red">1 year</strong>.</p>
        <p>Currently, I am looking for new opportunities as a <strong>Junior Python Developer</strong>.</p>
        <p>I live in <strong>Lausanne</strong>, canton of <strong>Vaud</strong>.</p>
        <p>I have permission to live and work in <strong>Switzerland</strong> (<strong style="color:red">Legitimation card R, Permission Ci</strong>).</p>
        <p>Unfortunately, I don't speak <strong>French</strong> and <strong>German</strong> (only <strong style="color:red">English</strong> and <strong style="color:red">Russian</strong>).</p>
        <p>My <strong>GitHub</strong> account - <strong>https://github.com/sergiishevchenko</strong></p>
        <p><strong><i style="color:blue">Should you require further information, please do not hesitate to contack me.</i></strong></p>
        <p><strong><i style="color:blue">Attached you can find the documents that may interest you.</i></strong></p>
        <p></p>
        <p></p>
        <p></p>
        <p>Best regards</p>
        <p><strong>Sergii Shevchenko</strong></p>
        <strong>mail:</strong> <strong>sergsheva1704@gmail.com<br></strong>
        <strong>telegram:</strong> <strong style="color:blue">@sergsheva</strong><br>
        <strong>tel.:</strong> <strong style="color:blue">+41778154379</strong>
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
