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
    path('readfeed/', views.read_feed, name="readfeed"),
    path('readfeed/<str:user>/', views.read_feed, name="readfeed"),
    path('profile/', views.profile_page, name="profile"),
    path('edit_profile/', views.update_profile, name='edit_profile'),
    path('delete_read/<int:pk>/', views.delete_read, name='delete_read'),
    path('books/', views.books, name='books'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('approve_book/<int:pk>/', views.approve_book, name='approve_book'),
    path('book_d/<int:pk>/', views.book_detail, name='book_detail'),
]
