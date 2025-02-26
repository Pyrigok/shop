from django.db import models


class UserRoles(models.TextChoices):
    CLIENT = "client", "Client"
    SELLER = "seller", "Seller"
    ADMIN = "admin", "Admin"
