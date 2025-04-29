from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Category
from .serializers import CategoriesSerializer
from .paginatsion import CategoryPagination


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer
    pagination_class = CategoryPagination
    permission_classes = [IsAuthenticated]