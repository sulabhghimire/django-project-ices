from django.urls import path
from .views import homepage, article_details, post_article, update_article, article_delete, search #importing our homepage function

urlpatterns = [
    path('', homepage, name="home"),
    path('articles-details/<int:pk>/', article_details, name='article_details'),
    path('post-article/', post_article, name='post'),
    path('post-update/<int:pk>', update_article, name='post_update'),
    path('post-delete/<int:pk>', article_delete, name='post_delete'),
    path('search/', search, name='search'),
]