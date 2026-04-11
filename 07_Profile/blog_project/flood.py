import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_project.settings')  # change project name
django.setup()

from django.contrib.auth.models import User
from blog.models import Article