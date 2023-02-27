from django.contrib import admin
from .models import Post


@admin.register(Post)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'modify_dt', 'tag_list', 'get_queryset']
    list_filter = ['modify_dt']
    search_fields = ['title', 'content', 'tags__name']  # TaggableManager에서 name으로 search_field 추가
    prepopulated_fields = {'slug': ('title',)}

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        """해당 포스트에 달린 태그의 모든 목록."""
        return u", ".join(o.name for o in obj.tags.all())
