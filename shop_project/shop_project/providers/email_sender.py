from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string


def send_email_template(to, subject, template, message=None, data=None):
    # data["support_email"] = settings.SUPPORT_EMAIL
    # data["platform_url"] = settings.PLATFORM_URL
    print('to - ', to)
    print('subject - ', subject)

    send_mail(
        subject=subject,
        html_message=render_to_string(template, data),
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[
            to,
        ],
        fail_silently=False,
        message=message,
    )
    print("email sent")
