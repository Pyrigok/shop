
from django.db import models

from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator, MinLengthValidator

from core.models import BaseModel
from users_app.constants import UserRoles


class User(AbstractUser, BaseModel):

    first_name = models.CharField(max_length=255, validators=[MinLengthValidator(2)], blank=True)
    last_name = models.CharField(max_length=255, validators=[MinLengthValidator(2)], blank=True)
    username = models.CharField(max_length=150, unique=False, editable=False)
    email = models.EmailField(validators=[EmailValidator()], unique=True)
    role = models.CharField(max_length=50, choices=UserRoles.choices)
    temporary_token = models.UUIDField(blank=True, null=True, verbose_name="Temporary token.")
    friends = models.ManyToManyField("users_app.User", blank=True, null=True)
    last_activity = models.DateTimeField(null=True)

    # for login
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f"{self.first_name} {self.last_name}. {self.role}"
