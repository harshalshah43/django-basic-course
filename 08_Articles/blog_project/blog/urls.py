from django.urls import path
from .views import (home,
                    about,
                    create_article,
                    update_article,
                    article_list,
                    article_detail,
                    delete_article)

urlpatterns = [
    path('home/',home,name='blog-home'),
    path('articles/', article_list, name='article_list'),
    path('about/',about),
    path('create-article/',create_article,name = 'create-article'),
    path('update-article/<int:id>/',update_article,name = 'update-article'),
    path('article/<int:id>/',article_detail,name = 'article-detail'),
    path('delete-article/<int:id>/',delete_article,name = 'delete-article')

    #careers 
    #newsletter
]