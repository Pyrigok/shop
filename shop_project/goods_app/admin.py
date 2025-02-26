from django.contrib import admin

from goods_app.models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title"]


class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "id", "price", "currency", "quantity", "is_visible"]
    ordering = ["title", "id", "price", "currency", "quantity", "is_visible"]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
