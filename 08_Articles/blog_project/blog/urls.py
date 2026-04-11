from django.urls import path
from .views import home,about,create_article

urlpatterns = [
    path('home/',home,name='blog-home'),
    path('about/',about),
    path('create-article/',create_article,name = 'create-article')
    #careers 
    #newsletter
]