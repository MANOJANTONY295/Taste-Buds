# utils.py

from django.core.mail import send_mail

def send_notification_email(subject, message, recipient_list):
    send_mail(subject, message, 'manojantony295@gmail.com', recipient_list, fail_silently=False)
