## This Django project was built inside a VM using vagrant


### Install
django=5.0.4
djangorestframework=3.15.1


### starting projects inside vagrant is slightly different
> venv needs to go to home directory which is /home/vagrant

#### generate and activate venv
python -m venv ~/venv
source ~/venv/bin/activate

> project file are in /vagrant directory which is different

#### Start project
django-admin startproject profiles_project .
#### Start app
python manage.py startapp profiles_api

#### Start server in VM using the exposed ip setup in vagrant file
python manage.py runserver 0.0.0.0:8000


#### Configue the custom user model
> at the botom of settings.py add

AUTH_USER_MODEL = 'profiles_api.UserProfile'


### CORS
#### Ref - https://www.stackhawk.com/blog/django-cors-guide/
##### first: ``` pip install django-cors-headers```
##### second: cors settings in istalled apps and middleware
``` django
INSTALLED_APPS = [
...
'corsheaders',
...
]

MIDDLEWARE = [
...,
'corsheaders.middleware.CorsMiddleware',
'django.middleware.common.CommonMiddleware',
...,
]

```
##### third: set allowed origins
``` django
 CORS_ALLOWED_ORIGINS = ['http://127.0.0.1'] 

 ```

