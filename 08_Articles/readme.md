# Check python version
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

# Create a new django-project
django-admin startproject blog_project

# Create new app
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

---

### 📌 Absolute vs Relative URLs in HTML

* **Absolute path (`/blog/home`)**
  Starts from the root of the website.
  Example:
  `/blog/home` → `http://127.0.0.1:8000/blog/home`
  ✅ Always reliable

* **Relative path (`blog/home`)**
  Appends to the current URL path.
  Example:
  Current page: `/user/login/`
  `blog/home` → `/user/login/blog/home`
  ❌ Can break depending on current location

* Browsers treat URLs like **file paths** and always keep a `/` between the domain and path, so invalid URLs like `http://127.0.0.1:8000blog/home` never occur.

* ✅ **Best practice in Django:**
  Use template tags:

  ```html
  {% url 'route_name' %}
  ```
---





Pratik - version control
python 3.11.9