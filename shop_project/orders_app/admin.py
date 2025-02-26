from django.contrib import admin

from orders_app.models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "client", "cost"]
    ordering = ["cost"]

    @staticmethod
    def client(order):
        return f"{order.user.first_name} {order.user.last_name}"


admin.site.register(Order, OrderAdmin)
