from django.urls import path, include
from rest_framework import routers

from goods_app import views


router = routers.SimpleRouter()

# goods
router.register("", views.ProductViewSet, basename="goods")

# specific good

urlpatterns = [
    path("", include(router.urls)),
]
