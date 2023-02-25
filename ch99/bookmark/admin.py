from django.contrib import admin
from bookmark.models import Bookmark
from blog.models import Post

@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url')
