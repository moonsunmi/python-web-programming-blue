from rest_framework import serializers, status
from .models import Blog


class PostListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ['title', 'slug', 'description', 'modify_dt']


class PostDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ['title', 'slug', 'description', 'content', 'create_dt', 'modify_dt']
