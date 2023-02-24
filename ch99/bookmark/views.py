from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from .models import Bookmark
from .serializers import BookmarkSerializer


class ListBookmarks(APIView):
    """Bookmark의 리스트를 보여주는 뷰"""


    def get(self, request):
        """모든 Bookmark가 담긴 리스트를 전달한다."""
        bookmarks = Bookmark.objects.all()
        serializer = BookmarkSerializer(bookmarks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DetailBookmark(APIView):
    """bookmark 하나의 자세한 정보를 보여 주는 뷰"""


    def get(self, request, pk):
        bookmark = get_object_or_404(Bookmark, pk=pk)
        serializer = BookmarkSerializer(bookmark)
        return Response(serializer.data, status=status.HTTP_200_OK )
