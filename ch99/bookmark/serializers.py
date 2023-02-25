from rest_framework import serializers
from .models import Bookmark


class BookmarkSerializer(serializers.ModelSerializer):
    """북마크 시리얼라이저"""

    class Meta:
        model = Bookmark
        fields = ['id', 'title', 'url']
