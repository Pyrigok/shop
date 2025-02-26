from django.db.models import Sum

from goods_app.models import Product
from orders_app.models import Order
from users_app.models import User



class OrderService:
    def __init__(self, user_id, items):
        self.user_id = user_id
        self.items = items

    def create_order(self, order_id):
        order = Order.objects.get(id=order_id)
        products = Product.objects.filter(id__in=self.items).values_list("id", flat=True)
        sum_price = products.aggregate(
            cost=Sum("price")
        )
        order.cost = sum_price["cost"]
        for item in products:
            order.products.add(item)
        order.save()

        from orders_app.tasks import send_order_letter
        send_order_letter.delay(self.user_id, order_id)

        # logger("order created")
