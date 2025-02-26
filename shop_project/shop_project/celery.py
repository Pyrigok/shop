import os

from celery import Celery
from django.conf import settings
from kombu import Queue

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop_project.settings")
app = Celery("shop_project")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.update(
    worker_pool_restarts=True,
)

app.conf.task_default_queue = "general"

app.conf.task_queues = (
    Queue("general"),
    Queue("order_creation_queue"),
    Queue("confirmation_email_queue"),
)
