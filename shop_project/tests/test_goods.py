import pytest

from goods_app.models import Category, Product

@pytest.mark.django_db
def test_product_creation():
    category = Category(
        title="title"
    )
    category.save()

    product = Product(
        title="title",
        category=category,
        price=10
    )
    product.save()

    test_product = Product.objects.get(id=product.id)
    assert product.title == test_product.title
