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
