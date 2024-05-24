# Deploy Workflow
1. Download the setup.sh into the server
2. add allowed Host in settings. (locally then git commit)
3. Update server codes
4. Createsuperuser

### Download setup.sh into the server and execute the shell script
```sh
curl -sL https://raw.githubusercontent.com/ballingj/drf_userprofile/main/deploy/setup.sh | sudo bash -

```

### Update settings.py locally
```python
ALLOWED_HOSTS = [
  '<ip-address of the server>',
   '127.0.0.1'
]   # 127.0.0.1 remains for local testing
```

### Update server codes
- commit changes to git and github
- run update script from the server
  -- navigate to project directory: should be '/usr/local/apps/profiles-rest-api'

```sh
sudo sh ./deploy/update.sh
```

### create Super User
```sh
sudo venv/bin/python manage.py createsuperuser
```

