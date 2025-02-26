
from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from information_app.models import Article
from information_app.serializers import ArticleSerializer
from permissions_app.constants import Permissions as user_permissions


class ArticlesView(APIView):
    # permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        articles = Article.objects.all().order_by("-created")
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ArticleView(APIView):
    # permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (user_permissions.ClientPermission,)

    def get(self, request, id):
        print("user - ", request.user)
        articles = Article.objects.get(id=id)
        serializer = ArticleSerializer(articles)
        return Response(serializer.data, status=status.HTTP_200_OK)
