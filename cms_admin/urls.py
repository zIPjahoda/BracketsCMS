from django.conf.urls import url
import django.contrib.auth

from cms_admin import views

urlpatterns = [
    # Index
    url(r'^index', views.index, name="index"),
    url(r'^$', views.index),

    # Navigation management
    url(r'^navigation-overview/$', views.navigation_overview, name="navigation-overview"),

    # Navigation management API actions
    url(r'^api/get-next-nav-item-id', views.api_get_next_nav_item_id, name="api-get-next-nav-item-id"),
    url(r'^api/add-nav-item', views.api_add_nav_item, name="api-add-nav-item"),
    url(r'^api/edit-nav-item/(?P<item_id>[0-9]+)/$', views.api_edit_nav_item, name="api-edit-nav-item"),
    url(r'^api/get-next-nav-item-id', views.api_get_next_nav_item_id, name="api-get-next-nav-item-id"),
    url(r'^api/edit-nav-item/(?P<item_id>[0-9]+)', views.api_edit_nav_item, name="api-edit-nav-item"),
    url(r'^api/delete-nav-item/(?P<item_id>[0-9]+)', views.api_delete_nav_item, name="api-delete-nav-item"),
    url(r'^api/add-empty-nav-item', views.api_add_empty_nav_item, name="api-add-empty-nav-item"),

    # Post management
    url(r'^post/edit/(?P<url>[\w-]+)/$', views.post_edit, name='post_edit'),
    url(r'^post/detail/(?P<url>[\w-]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/delete/(?P<url>[\w-]+)/$', views.post_delete, name='post_delete'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/overview/$', views.post_overview, name="post_overview"),

    # Category management
    url(r'^category/edit/(?P<url>[\w-]+)/$', views.category_edit, name='category_edit'),
    url(r'^category/detail/(?P<url>[\w-]+)/$', views.category_detail, name='category_detail'),
    url(r'^category/delete/(?P<url>[\w-]+)/$', views.category_delete, name='category_delete'),
    url(r'^category/create/$', views.create_category, name='create_category'),
    url(r'^category/overview/$', views.category_overview, name="category_overview"),


    # Static page management
    url(r'^static-page/$', views.static_page_overview, name="static_page_overview"),
    url(r'^static-page/detail/(?P<url>[\w-]+)/$', views.static_page_detail, name="static_page_detail"),
    url(r'^static-page/overview/$', views.static_page_overview, name="static_page_overview"),
    url(r'^static-page/add/$', views.new_static_page, name="static_page_add"),
    url(r'^static-page/edit/(?P<url>[\w-]+)/$', views.static_page_edit, name="static_page_edit"),
    url(r'^static-page/delete/(?P<url>[\w-]+)/$', views.static_page_delete, name="static_page_delete"),

    # Users
    url(r'^login', views.login, name="user_login"),
    url(r'^login/', views.login),
    url(r'^register/', views.register, name="user_register"),
    url(r'^logout', views.logout, name="user_logout"),
]
