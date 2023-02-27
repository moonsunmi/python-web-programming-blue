from django.urls import path, re_path
from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.PostListView.as_view(), name='index'),  # /blog/
    path('post/', views.PostListView.as_view(), name='post_list'),  # /blog/post/
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),  # /blog/post/<slug>/
    # 하단은 slug의 한글 구현을 위한 것. 그러나 작동되지 않는다.
    # re_path(r'^post/(?P<slug>[-w]+)/$', views.PostDetailView.as_view(), name='post_detail'),
    path('archive/', views.PostArchiveView.as_view(), name='post_archive'),
    path('archive/<int:year>', views.PostYearArchiveView.as_view(), name='post_year_archive'),
    path('archive/<int:year>/<int:month>/', views.PostMonthArchiveView.as_view(), name='post_month_archive'),
    path('archive/<int:year>/<int:month>/<int:day>/',
         views.PostDayArchiveView.as_view(), name='post_month_archive'),
    path('archive/today/', views.PostTodayArchiveView.as_view(), name='post_today_archive'),
]
