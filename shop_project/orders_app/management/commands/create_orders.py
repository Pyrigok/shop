from django.core.management import BaseCommand
from django.db.models import Sum

from goods_app.models import Category, Product
from orders_app.models import Order
from users_app.models import User


class Command(BaseCommand):

    def handle(self, *args, **options) -> None:
        self.stdout.write(self.style.SUCCESS("Orders creation start!"))

        users = User.objects.all()

        def fill_orders(
                users_start_index, user_finish_index,
                order_start_index, order_finish_index,
        ):

            product_ids = range(order_start_index, order_finish_index)
            for user in users[users_start_index:user_finish_index]:
                order = Order.objects.create(
                    user=user,
                )
                order.save()

                products = Product.objects.filter(id__in=product_ids)
                cost = products.aggregate(cost=Sum("price"))
                for item in products:
                    order.products.add(item)
                    order.cost=cost["cost"]
                order.save()

        fill_orders(0, 10, 0, 30)
        fill_orders(11, 20, 31, 90)
        fill_orders(21, 30, 91, 125)

        self.stdout.write(self.style.SUCCESS("Done!"))
