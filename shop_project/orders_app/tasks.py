from shop_project.celery import app
from orders_app.services import OrderService
from shop_project.providers.email_sender import send_email_template

from users_app.models import User


@app.task(name="order_creation", queue="order_creation_queue")
def create_order_task(user_id, order_id, items):
    OrderService(user_id, items).create_order(order_id)


@app.task(name="confirmation_email_queue", queue="confirmation_email_queue")
def send_order_letter(user_id, order_id):
    user = User.objects.get(id=user_id)
    message = "Your order was accepted successfully."
    send_email_template(user.email, "Order creation", "orders/accepted_order.html", message=message)
