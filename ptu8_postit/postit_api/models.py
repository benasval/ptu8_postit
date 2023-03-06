from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=150)
    body = models.CharField(max_length=2000)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ['-created']


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    body = models.CharField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ['-created']

    def __str__(self) -> str:
        return f"{self.id}, {self.body[:100]}"


class PostLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_likes")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")


class CommentLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_likes")
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="likes")
