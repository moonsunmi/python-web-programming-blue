from rest_framework import serializers, status
from .models import Post


class PostListSerializer(serializers.ModelSerializer):
    """블로그 앱 포스트의 리스트 시리얼라이저"""

    class Meta:
        model = Post
        fields = ['title', 'slug', 'description', 'modify_dt']


class PostDetailSerializer(serializers.ModelSerializer):
    """블로그 앱 포스트 하나의 디테일 시리얼라이저"""
    # previous_by_modify_dt = serializers.CharField(source='get_previous', read_only=True)
    # next_by_modify_dt = serializers.CharField(source='get_next', read_only=True)
    absolute_url = serializers.URLField(source='get_absolute_url', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'description', 'content',
                  'modify_dt', 'create_dt', 'absolute_url']
        # 'previous_by_modify_dt', 'next_by_modify_dt']
