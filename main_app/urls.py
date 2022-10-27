from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import MeView

urlpatterns = [
    path('', views.home, name='home'),
    path('instruments/', views.instruments, name='instruments'),
    path('students/', views.students, name='students'),
    path('teachers/', views.teachers, name='teachers'),
    path('users/', views.users, name='users'),
    path('reviews/', views.reviews, name='reviews'),
    path('inquiries/', views.inquiries, name='inquiries'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('me/', MeView.as_view(), name='me'),
]