from django.conf.urls import url
from django.contrib.sitemaps import views
from . import views
from . import rss

urlpatterns = [
    # The homepage.
    url(r'^$', views.home, name="home"),

    # A post (Article model)
    url(r'^post/(?P<url>[\w-]+)/$', views.post_detail, name='post_detail'),

    # A category (Category model)
    url(r'^category/(?P<url>[\w-]+)/$', views.category_detail, name='category_detail'),

    # A static page (StaticPage model)
    url(r'^(?P<url>[\w-]+)/$', views.page_detail, name="page_detail"),

    url(r'^feed/rss/$', rss.LatestPosts()),
]

