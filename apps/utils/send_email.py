import smtplib
from email import charset
from email.generator import Generator
from email.header import Header

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from io import StringIO
from django.conf import settings
from django.core.mail import send_mail


def send_mail_user(user_mail, subject, html_template):
    send_mail(
        subject,
        html_template,
        from_email="はたらきナース <{}>".format(settings.EMAIL_HOST_USER),
        recipient_list=[user_mail],
        fail_silently=True
    )