from django.core.mail import send_mail
from django.conf import settings


def send_email(email, token):
    subject = 'An anonymous device Loged in to your gmail'
    message = f'Click on the link to see that device and change your gmail password http://127.0.0.1:8000/gmail.com/{token}/'
    email_from = settings.EMAIL_HOST_USER
    recipien_list = [email]
    send_mail(subject, message, email_from, recipien_list)
    return True