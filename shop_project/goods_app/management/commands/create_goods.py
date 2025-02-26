from django.core.management import BaseCommand

from goods_app.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options) -> None:
        self.stdout.write(self.style.SUCCESS("Categories creation start!"))
        for item in range(10):
            data = {
                "title": f"category {item}"
            }
            category = Category.objects.create(
                **data
            )
            category.save()
            self.stdout.write(self.style.SUCCESS(f"Categoty {item} created"))

        self.stdout.write(self.style.SUCCESS("Goods creation start!"))
        for category in Category.objects.all():
            for item in range(10):
                data = {
                    "category": category,
                    "title": f"product {item}",
                    "description": f"{item}",
                    "currency": "гривня",
                    "price": f"{item}",
                    "quantity": f"{item}",
                    "is_visible": True,
                }
                product = Product.objects.create(
                    **data
                )
                product.save()
                self.stdout.write(self.style.SUCCESS(f"Product {item} created"))

        self.stdout.write(self.style.SUCCESS("Done!"))