from django.db import models

from core.models import BaseModel


class Order(BaseModel):
    user = models.ForeignKey(to="users_app.User", on_delete=models.CASCADE)
    products = models.ManyToManyField("goods_app.Product")
    cost = models.PositiveIntegerField(null=True)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return f"{self.id}"
