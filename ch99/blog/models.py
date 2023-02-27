from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField('TITLE', max_length=100)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.')
    description = models.CharField('DESCRIPTION', max_length=200, blank=True)
    content = models.TextField('CONTENT')
    create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)  # 최초에만 now가 add.
    modify_dt = models.DateTimeField('MODIFY DATE', auto_now=True)  # 수정될 때마다 now가 변경되는 것

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = 'blog_posts'
        ordering = ('-modify_dt',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=(self.slug,))

#    previous, next object가 없을 때 어떻게 처리해야 할까?
#    def get_previous(self):
#        """수정 날짜(modify_dt)를 기준으로 이 포스트보다 앞에 있는 포스트의 '제목'(title)을 반환한다."""
#        return self.get_previous_by_modify_dt()

#    def get_next(self):
#        """수정 날짜(modify_dt)를 기준으로 이 포스트보다 뒤에 있는 포스트의 '제목'(title)을 반환한다."""
#        return self.get_next_by_modify_dt()
