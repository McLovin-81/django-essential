# To install django use the following commands
```
python3 -m pip install django
python3 -m pip install black
```

# Create a new django project (Settings folder) using the following command.
```
django-admin startproject projectName .
````
The following folder/files will be created:
- projectName
    - __init__.py
    - asgi.py
    - settings.py
    - urls.py
    - wsgi.py
- manage.py

# Run a server, using the default configuration.
```
python3 manage.py runserver
```

# Use the following command to create a new app.
```
django-admin startapp app1
```
The following folder/files will be created:
- app1
    - migrations
        - __init__.py
    - __init__.py
    - admin.py
    - apps.py
    - models.py
    - tests.py
    - views.py

## Every time an app has been created, the app must be added to the settings folder!
- projectName
    - settings.py -> INSTALLED_APPS
```
"app1"
```

# Create a view.
- app1
    - views.py
```
from django.http import HttpResponse

def app1(request):
    return HttpResponse("Hello, world!")
```
- projectName
    - urls.py
```
from app1 import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("app1", views.app1),
]
```

# Return HTML pages.
1. Create a folder (templates) inside an app folder.
2. Inside the templates folder, create a new folder (app1).
3. Inside the app1 folder create a HTML file.

- app1
    - templates
        - welcome.html

4. Write a function to render HTML page in views.py
```
def app1(request):
    return render(request, "app1/welcome.html", {})
```
- app1
    - views.app

# Passing down information.
1. Write a function in views.py
```
from django.http import HttpResponse
from datetime import datetime

def app1(request):
    return render(request, "app1/welcome.html", {"today": datetime.today()})
```
2. Add the information in the html file.
```
<html>
    <header>
        <title>App1</title>
    </header>

    <body>
        <h1>Welcome to app1</h1>
        <p>Today is {{today}}</p>
    </body>
</html>
```

# Eliminate dependencies
1. Create a file named urls.py in app folder.
```
from django.urls import path

from . import views


urlpatterns = [
    path("app1", views.app1),
]
```
2. In the project folder -> urls.py:
    - Delete all dependencies with app1
3. Import the include function
4. Add an import path but instead of using an app-function it should be a django function -> include
''' 
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("app1.urls")),
]
```