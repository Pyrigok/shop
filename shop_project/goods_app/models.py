from django.db import models

from core.models import BaseModel


class Category(BaseModel):
    title = models.CharField()
    description = models.CharField(blank=True, null=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class Product(BaseModel):
    category = models.ForeignKey(to="goods_app.Category", on_delete=models.DO_NOTHING)
    title = models.CharField()
    description = models.CharField()
    currency = models.CharField()
    price = models.PositiveIntegerField()
    image = models.ImageField(
        blank=True,
        null=True,
        upload_to="products/",
        verbose_name="Product image",
    )
    quantity = models.PositiveIntegerField(default=0)
    is_visible = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.title
