### Install
django=5.0.4
drangorestframework=3.15.1



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