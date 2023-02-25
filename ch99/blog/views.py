from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Blog
from .serializers import PostListSerializer, PostDetailSerializer


class PostListView(APIView):
    def get(self, request):
        posts = Blog.objects.all()
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostDetailView(APIView):

    def get(self, request, slug):
        post = get_object_or_404(Blog, slug=slug)  # < slug=slug 맞는지 모르겠음.
        serializer = PostDetailSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)
