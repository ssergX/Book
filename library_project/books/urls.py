from django.urls import include, path
from .views import BookViewSet

urlpatterns = [
    path('books', views.BookViewSet.as_view(), name='book'),
]
