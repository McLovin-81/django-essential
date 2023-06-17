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

4. Write function to render HTML page in views.py
```
def app1(request):
    return render(request, "app1/welcome.html", {})
```
- app1
    - views.app

# Passing down information.