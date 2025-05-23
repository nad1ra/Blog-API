from django.urls import path
from .views import RegisterView, LoginView, LogoutView, RefreshTokenView, UserProfileView

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('api/auth/login/', LoginView.as_view(), name='login'),
    path('api/auth/logout/', LogoutView.as_view(), name='logout'),
    path('api/auth/refresh/', RefreshTokenView.as_view(), name='refresh_token'),
    path('api/users/me/', UserProfileView.as_view(), name='user_profile'),
]


