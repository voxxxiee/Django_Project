from django.urls import path, include
from . import views

app_name = 'base'

urlpatterns = [
    path('', views.index, name='index'),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('bookform/', views.add_book, name="bookform"),
    path('bookform/<int:pk>/', views.add_book, name="bookform"),
    path('readform/', views.add_read, name="readform"),
    path('readform/<int:pk>/', views.add_read, name="readform"),
]
