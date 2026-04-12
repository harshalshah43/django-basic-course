from django.urls import path
from .views import home,about,create_article,article_view

urlpatterns = [
    path('home/',home,name='blog-home'),
    path('articles/', article_view, name='article-view'),
    path('about/',about),
    path('create-article/',create_article,name = 'create-article')
    #careers 
    #newsletter
]