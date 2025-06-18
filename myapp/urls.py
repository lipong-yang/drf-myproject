from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookListCrete,BookDetail,Register 

router = DefaultRouter()

urlpatterns = [
    path('book/', BookListCrete.as_view(), name = 'book-list-create'),
    path('books/<int:pk>/', BookDetail.as_view(), name = 'book-detail'),
    path('register/', Register.as_view(), name = 'register')
]