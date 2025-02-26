from django.db.models import OuterRef, Subquery
from django.shortcuts import render
from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie

from rest_framework import viewsets, response, status, permissions
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

from goods_app import serializers, models


class ProductViewSet(viewsets.ViewSet):
    # queryset = models.Product.objects.all()
    # serializer = serializers.ProductSerializer(queryset, many=True)
    pagination_class = LimitOffsetPagination
    permission_classes = (permissions.AllowAny,)
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer,)
    template_name = "goods/products.html"

    def list(self, request):
        products = models.Product.objects.filter(is_visible=True)
        serializer = serializers.ProductSerializer(products, many=True)

        # for testing in postman
        return response.Response(serializer.data, status=status.HTTP_200_OK)
        # for html template
        # return render(request, "users/users.html", {"users": serializer.data})

    @method_decorator(cache_page(60 * 5))
    @method_decorator(vary_on_cookie)
    @action(detail=False, methods=["get"], url_path="first-products")
    def first_products(self, request):
        """Get newest product from each category."""

        first_products = cache.get("first_products")
        # first_products = None
        print("from cache - ", first_products)

        if not first_products:
            latest_product = models.Product.objects.filter(
                is_visible=True,
                category=OuterRef('category')
            ).order_by('-created').values('id')[:1]
            first_products = models.Product.objects.filter(id__in=Subquery(latest_product))
            print("from DB - ", first_products)
            cache.set("first_products", first_products)

        serializer = serializers.ProductSerializer(first_products, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)
