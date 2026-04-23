from django.db import models
from django.contrib.auth.models import User
import os

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()

    author = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    image = models.ImageField(upload_to='article_pics/',blank=True,null=True)

    category_choices = (('','Select Category'),
                        ('technology','Technology'),
                        ('lifestyle','Lifestyle'),
                        ('coding','Coding'))

    category = models.CharField(max_length=25, choices=category_choices,blank = False)

    def __str__(self):
        return f"{self.title}"
    
    def save(self, *args, **kwargs):
        try:
            old_instance = Article.objects.get(id=self.id)

            if old_instance.image and old_instance.image != self.image:
                if os.path.isfile(old_instance.image.path):
                    os.remove(old_instance.image.path)

        except Article.DoesNotExist:
            pass

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)

        super().delete(*args, **kwargs)

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name= 'comment')
    user = models.ForeignKey(User, on_delete= models.DO_NOTHING)

    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commented by {self.user.username} at {self.created_at}"