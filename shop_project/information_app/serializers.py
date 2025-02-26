from rest_framework import serializers
from tutorial.quickstart.serializers import UserSerializer

from information_app.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
