from datetime import datetime as dt, timedelta
from time import strptime, strftime

from django.db.models import Subquery, OuterRef
from rest_framework import viewsets, response, status, permissions
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.viewsets import GenericViewSet

from orders_app.models import Order
from orders_app.serializers import CreateOrderSerializer, OrderSerializer
from users_app.models import User


# class ManageOrderViewSet(viewsets.ViewSet):
class ManageOrderViewSet(CreateModelMixin, GenericViewSet):
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.AllowAnyd]
    serializer_class = CreateOrderSerializer
    pagination_class = LimitOffsetPagination
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer,)
    # template_name = "orders/create_order.html"

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(status=status.HTTP_201_CREATED)

    def list(self):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)


class OrderViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    pagination_class = LimitOffsetPagination

    @action(detail=False, methods=["get"], url_path="daily-orders")
    def daily_orders(self, request):
        # orders = User.objects.filter(user_id=OuterRef("order")).values("id")
        today = dt.today().date()
        filter_date = today - timedelta(days=1)
        orders = Order.objects.filter(
            # id__in=Subquery(orders),
            created__date=filter_date
        ).order_by("user", 'cost')
        serializer = OrderSerializer(orders, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)
