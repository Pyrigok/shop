from django.contrib import admin

from information_app.models import Comment, Article


class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "evaluation",)

    def user(self, comment):
        return f"{comment.author.first_name} {comment.author.last_name}"


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "subscription",)
    ordering = ("title", "subscription",)

    def user(self, article):
        return f"{article.author.first_name} {article.author.last_name}"

admin.site.register(Comment, CommentAdmin)
admin.site.register(Article, ArticleAdmin)
