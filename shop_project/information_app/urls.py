from django.urls import path


from information_app import views


# create comment
# list by product
urlpatterns = [
    path("articles/", views.ArticlesView.as_view(), name="articles"),
    path("articles/<int:id>/", views.ArticleView.as_view(), name="article"),
    # path("comments/", CommentsViewSet.as_view(), name="comments")
]
