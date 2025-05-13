import smtplib
from email.message import EmailMessage

def send_email(to_email, subject, body):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = 'your_email@example.com'
    msg['To'] = to_email
    msg.set_content(body)

    # For Gmail, use smtp.gmail.com and enable "less secure apps" or use App Password
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('your_email@example.com', 'your_password')
        smtp.send_message(msg)
        print("Email sent!")

