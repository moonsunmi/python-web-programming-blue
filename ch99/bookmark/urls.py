from django.urls import path
from .views import ListBookmarks, DetailBookmark


urlpatterns = [
    path('', ListBookmarks.as_view()),
    path('<int:pk>/', DetailBookmark.as_view()),
]
