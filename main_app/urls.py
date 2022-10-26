from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('instruments/', views.instruments, name='instruments'),
    path('students/', views.students, name='students'),
    path('teachers/', views.teachers, name='teachers'),
    path('reviews/', views.reviews, name='reviews'),
    path('inquiries/', views.inquiries, name='inquiries'),
]