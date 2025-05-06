from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostLikeViewSet

router = DefaultRouter()
router.register(r'post-likes', PostLikeViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
