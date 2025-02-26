from django.urls import path, include
from rest_framework import routers

from orders_app.views import ManageOrderViewSet, OrderViewSet

router = routers.SimpleRouter()

router.register("manage", ManageOrderViewSet, basename="manage-orders")
router.register("", OrderViewSet, basename="orders")

# make order (websocket, celery, redis)

# orders by user

# specific user's order

# most ordered goods for specific period (month, week, day) (for all users, specific user)

urlpatterns = [
    path("", include(router.urls)),
]