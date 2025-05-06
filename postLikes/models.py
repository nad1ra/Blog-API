from django.db import models
from posts.models import Post
from userProfiles.models import User


class PostLike(models.Model):
    VALUE_CHOICES = [
        ('like', 'Like'),
        ('dislike', 'Dislike'),
    ]
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='postlike')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='postlike')
    created_at = models.DateTimeField(auto_now_add=True)
    value = models.CharField(max_length=10, choices=VALUE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.value} - {self.post.title}"