"""
Reusable code snippet for Python3.4+
"""

__author__ = 'daniel zhou, danithaca@gmail.com'


def send_email(subject, body, email_from, email_to):
    import smtplib
    from email.mime.text import MIMEText

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = email_from    # e.g. abc@example.com
    msg['To'] = email_to

    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()


if __name__ == '__main__':
    print('This is not a stand-alone script.')