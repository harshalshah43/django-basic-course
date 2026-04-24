from django.db import models
from django.contrib.auth.models import User
import os
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pics/default.jpeg', upload_to='profile_pics')

    def __str__(self):
        return f"{self.user.username} Profile"

    def save(self, *args, **kwargs):
        old_profile = Profile.objects.get(id = self.id)

        if old_profile.image and old_profile.image != self.image:
            if os.path.isfile(old_profile.image.path):
                os.remove(old_profile.image.path)
        
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)

        super().delete(*args, **kwargs)