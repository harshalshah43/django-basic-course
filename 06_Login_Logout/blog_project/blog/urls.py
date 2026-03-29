from django.urls import path
from .views import home,about

urlpatterns = [
    path('home/',home,name='blog-home'),
    path('about/',about),

    #careers 
    #newsletter
]