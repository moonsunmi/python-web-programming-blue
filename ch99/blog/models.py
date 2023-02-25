from django.db import models


class Blog(models.Model):
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

    # 기타 get_absolute_url 같은 것들 추가해야 함.
