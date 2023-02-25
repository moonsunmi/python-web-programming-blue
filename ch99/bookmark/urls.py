from django.urls import path
from .views import ListBookmarks, DetailBookmark


app_name = 'bookmark'
urlpatterns = [
    path('', ListBookmarks.as_view(), name='index'),
    path('<int:pk>/', DetailBookmark.as_view(), name='detail'),
]
