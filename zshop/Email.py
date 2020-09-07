from django.core.mail import send_mail
from django.conf import settings
from zshop.settings import EMAIL_HOST_USER, EMAIL_HOST, EMAIL_HOST_PASSWORD

class Email:
    def __init__(self, subject = '', message = '', email = '', target_list = []):
        self.subject = subject
        self.message = message
        self.email = email
        self.target_list = target_list

    def send(self):
        print(EMAIL_HOST_USER, EMAIL_HOST, EMAIL_HOST_PASSWORD)
        send_mail(self.subject, self.message, self.email, self.target_list)