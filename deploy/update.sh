#!/usr/bin/env bash

set -e

PROJECT_BASE_PATH='/usr/local/apps/profiles-rest-api'

cd $PROJECT_BASE_PATH
git pull
$PROJECT_BASE_PATH/venv/bin/python manage.py migrate
$PROJECT_BASE_PATH/venv/bin/python manage.py collectstatic --noinput
supervisorctl restart profiles_api

echo "DONE! :)"
