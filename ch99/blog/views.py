from django.utils import timezone
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Post
from .serializers import PostListSerializer, PostDetailSerializer


class PostListView(APIView):
    """포스트의 목록 뷰."""
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostDetailView(APIView):
    """포스트의 상세 페이지 뷰."""

    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        serializer = PostDetailSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostArchiveView(APIView):
    """포스트 아카이브 목록 뷰.
    현재는 Post List와 같은 상태. PostList와 어떤 점을 다르게 구현해야 하는 걸까?"""

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostYearArchiveView(APIView):
    """포스트 연(year) 단위 아카이브 뷰."""

    def get(self, request, year):
        posts = Post.objects.filter(modify_dt__year=year)
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostMonthArchiveView(APIView):
    """포스트 월(month) 단위 아카이브 뷰."""

    def get(self, request, year, month):
        posts = Post.objects.filter(modify_dt__year=year).filter(modify_dt__month=month)
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostDayArchiveView(APIView):
    """포스트 일(day) 단위 아카이브 뷰."""

    def get(self, request, year, month, day):
        posts = Post.objects.filter(modify_dt__year=year).filter(modify_dt__month=month).filter(modify_dt__day=day)
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostTodayArchiveView(APIView):
    """포스트 오늘의(today) 아카이브 뷰."""

    def get(self, request):
        posts = Post.objects.filter(modify_dt__date=timezone.localtime().date())
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
