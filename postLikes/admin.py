from django.contrib import admin
from .models import PostLike


@admin.register(PostLike)
class PostLikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'user', 'created_at', 'value')
    search_fields = ('post', 'user', 'created_at')