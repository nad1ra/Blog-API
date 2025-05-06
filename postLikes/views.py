from django.contrib.admin import action
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import PostLike
from .serializers import PostLikeSerializer
from .models import Post


class PostLikeViewSet(viewsets.ModelViewSet):
    queryset = PostLike.objects.all()
    serializer_class = PostLikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        post = serializer.validated_data['post']
        user = self.request.user

        if PostLike.objects.filter(post=post, user=user).exists():
            raise serializer.ValidationError("You have already liked or disliked this post.")

        serializer.save(user=user)

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):

        post = self.get_object()
        user = request.user

        like_instance, created = PostLike.objects.get_or_create(post=post, user=user)

        if 'value' not in request.data or request.data['value'] not in ['like', 'dislike']:
            return Response({"detail": "Value must be 'like' or 'dislike'."}, status=status.HTTP_400_BAD_REQUEST)

        like_instance.value = request.data['value']
        like_instance.save()

        return Response(PostLikeSerializer(like_instance).data, status=status.HTTP_200_OK)

