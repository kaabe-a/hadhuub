from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap
sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
    path('',views.post_list,name='posts'),
    path('posts/create/',views.post_create,name='post-create'),
    path('posts/<str:slug>/',views.post_detail,name='post-detail'),
    path('posts/<str:pk>/delete/',views.post_delete,name='post-delete'),
    path('posts/<str:pk>/update/',views.post_update,name='post-update'),
    path('posts/<str:category>/category/',views.post_category,name='post-category'),
    path('posts/<str:tag>/tag/',views.post_by_tag,name='post-tag'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
]
