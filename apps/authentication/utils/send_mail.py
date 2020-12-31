import math
import random
import threading

from django.conf import settings
from django.core.mail import send_mail
from django.template import loader

from apps.authentication.models import UserAuth
from apps.utils.config import MailSubject, OTPCode
from apps.utils.constants import AuthType, OrderStatusType


class EmailTemplate:

    def generate_otp(self, user, auth_type):
        digits = OTPCode.otp_string
        otp_code = ""
        # length of password can be changed
        # by changing value in range
        for i in range(6):
            otp_code += digits[math.floor(random.random() * 10)]

        # save OTP code
        UserAuth.objects.create(
            user=user,
            auth_code=otp_code,
            auth_type=auth_type
        )

        return otp_code

    def get_context(self, user, auth_type):
        context = dict()
        context['user_name'] = user.username
        context['code'] = self.generate_otp(user, auth_type)
        return context

    def send_activation_email(self, user):
        context = self.get_context(user, AuthType.ACTIVATION.value)
        html_message = loader.render_to_string(
            'activation_email.html', context
        )
        thread_sendmail = threading.Thread(
            target=self.send_mail_user,
            args=(user.email, MailSubject.activation, html_message,),
            name='send_activation_email'
        )
        thread_sendmail.start()

    def send_forgot_password_email(self, user):
        context = self.get_context(user, AuthType.FORGOT_PASSWORD.value)
        html_message = loader.render_to_string(
            'forgot_password_email.html', context
        )
        thread_sendmail = threading.Thread(
            target=self.send_mail_user,
            args=(user.email, MailSubject.forgot_password, html_message,),
            name='send_forgot_password_email'
        )
        thread_sendmail.start()

    def send_completed_order_email(self, user):
        context = self.get_context(user, OrderStatusType.COMPLETED.value)
        html_message = loader.render_to_string(
            'complete_order.html', context
        )
        thread_sendmail = threading.Thread(
            target=self.send_mail_user,
            args=(user.email, MailSubject.completed_order, html_message,),
            name='send_completed_order_email'
        )
        thread_sendmail.start()

    @staticmethod
    def send_mail_user(user_mail, subject, html_template):
        send_mail(
            subject,
            '',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user_mail],
            html_message=html_template,
            fail_silently=True
        )