### Create project

```
 django-admin startproject djangotryout
```

### Create app

```
 python manage.py startapp firstapp
```

### Register models changes to your application

```
 python manage.py makemigrations first_app
```

### Run migration

```
 python manage.py migrate
```

#### Run Shell

```
 python manage.py shell
```

```
Python 3.5.2 (default, Nov 17 2016, 17:05:23)
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from first_app.models import Topic
>>> print(Topics.objects.all())
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'Topics' is not defined
>>> print(Topic.objects.all())
<QuerySet []>
>>> t = Topic(top_name="Adventure")
>>> t.save()
>>> print(Topic.objects.all())
<QuerySet [<Topic: Adventure>]>
>>>

```


#### Create super user
```
 python manage.py createsuperuser
```
