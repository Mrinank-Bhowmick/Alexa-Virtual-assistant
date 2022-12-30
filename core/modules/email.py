import smtplib
from email.message import EmailMessage

def send_email(to, content):
    msg = EmailMessage()
    msg['Subject'] = 'This is a test email'
    msg.set_content(content)
    msg['From'] = 'your email'
    msg['To'] = to  
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('your email', 'your password')
    server.send_message(msg)
    server.quit()
    return 'Email sent successfully'
