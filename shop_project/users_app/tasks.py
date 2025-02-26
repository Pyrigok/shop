from django.conf import settings


from shop_project.providers.email_sender import send_email_template

from shop_project.celery import app
from users_app.models import User


@app.task(name="confirmation_email", queue="confirmation_email_queue")
def send_registration_mail(user_id):
    user = User.objects.get(id=user_id)
    sign_up_link = f"https://{settings.DEFAULT_FRONT_DOMAIN}/signup/{user.temporary_token}"
    data = {
        "name": user.first_name,
        "user_email": user.email,
        "link": sign_up_link,
    }
    send_email_template(
        user.email,
        "Profile activation",
        "email/activate_email.html",
        data
    )
