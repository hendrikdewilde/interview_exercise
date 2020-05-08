#!/usr/bin/env bash
cd /vagrant/
PATH=/usr/local/bin:$PATH
pipenv run python3 /vagrant/manage.py makemigrations
pipenv run python3 /vagrant/manage.py migrate
pipenv run python3 /vagrant/manage.py runserver 0.0.0.0:8002
