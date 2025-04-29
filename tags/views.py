from rest_framework import viewsets
from .models import Tag
from .serializers import TagSerializer
from .permissions import IsAdminOrReadOnly
from .paginations import TagPagination

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = TagPagination
    permission_classes = [IsAdminOrReadOnly]
