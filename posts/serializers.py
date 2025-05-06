from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post.objects.all()
        fields = ['id', 'title', 'slug', 'content']