from django.db import models

from core.models import BaseModel


class SubscriptionType(models.TextChoices):
    FREE = "free"
    DAILY = "daily", "Daily"
    MONTHLY = "monthly", "Monthly"
    ANNUAL = "annual", "Annual"


class Article(BaseModel):
    title = models.CharField()
    description = models.TextField(max_length=500)
    author = models.ForeignKey(to="users_app.User", on_delete=models.CASCADE)
    subscription = models.CharField(
        choices=SubscriptionType.choices,
        max_length=64,
        blank=True,
        default=SubscriptionType.FREE,
    )

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def __str__(self):
        return f"{self.title}, {self.author.username}"



class Comment(BaseModel):
    author = models.ForeignKey(to="users_app.User", on_delete=models.CASCADE)
    product = models.ForeignKey(to="goods_app.Product", on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    evaluation = models.PositiveIntegerField(default=5)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return f"{self.title}, {self.author.username}"
