# check python version
python --version

# Create virtul env
python -m venv dj
dj\Scripts\activate.bat
CAUTION: once virtual env directory is created don't move it or copy it anywhere

# Installation of packages: pip list

pip install Django
pip install requests

# Info 
manage.py -> basedir
settings.py -> projdir

# create a new django-project
django-admin startproject blog_project

# create new app
python manage.py startapp

# Run Project
python manage.py runserver

# How to add 2 webpages Home and About
- Added urls.py file in blog
- Created 2 view function for handling httpresposne for home and about
- added their paths in urls.py
- In urls.py file of project directory imported include and added path('blog',include('blog.urls'))

# Explanation
- Http request gets routed first from the project-urls.py from there it gets further mapped to blog urls depending on what is the url pattern










Pratik - version control
python 3.11.9