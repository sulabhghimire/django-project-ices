from django.urls import path
from .views import homepage, article_details, post_article #importing our homepage function

urlpatterns = [
    path('', homepage, name="home"),
    path('articles-details/<int:pk>/', article_details, name='article_details'),
    path('post-article/', post_article, name='post'),
]