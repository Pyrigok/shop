from typing import Dict

from prompt_toolkit.validation import ValidationError
from rest_framework import serializers

from goods_app.models import Product
from goods_app.serializers import ProductSerializer
from orders_app.models import Order
from orders_app.tasks import create_order_task


class CreateOrderSerializer(serializers.Serializer):
    items = serializers.ListField(
        child=serializers.IntegerField(),
        required=True,
    )

    def validate(self, data):
        for item in data["items"]:
            if not Product.objects.filter(id=item).exists():
                raise ValidationError(f"Product with id {item} does not exist!")
        return data

    def create(self, validated_data: Dict):
        user = self.context["request"].user
        items = validated_data["items"]
        order = Order(
            user=user,
        )
        order.save()
        create_order_task.delay(user.id, order.id, items)
        return order


class OrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    class Meta:
        model = Order
        exclude = ("updated",)
