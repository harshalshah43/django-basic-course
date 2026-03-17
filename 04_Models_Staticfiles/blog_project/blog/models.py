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

    def __str__(self):
        return f"{self.title}"

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name= 'comment')
    user = models.ForeignKey(User, on_delete= models.DO_NOTHING)

    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commented by {self.user.username} at {self.created_at}"