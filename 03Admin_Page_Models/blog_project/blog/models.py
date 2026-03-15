from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()

    author = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    image = models.ImageField(upload_to='article_pics/',blank=True,null=True)

    category_choices = (('technology','Technology'),
                        ('lifestyle','Lifestyle'),
                        ('coding','Coding'))

    category = models.CharField(max_length=25, choices=category_choices)

