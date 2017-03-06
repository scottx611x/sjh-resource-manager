# sjh-resource-manager
Django app to handle AWS resource management of https://github.com/hms-dbmi/scalable-jupyter-hosting

## Pre-reqs:
- Assumes [virtualenvwrapper](http://virtualenvwrapper.readthedocs.io/en/latest/install.html) is installed.
- python 2.7.x, 3.4, 3.5
- pip

## Installation:

```
git clone https://github.com/scottx611x/sjh-resource-manager.git && cd sjh-resource-manager
mkvirtualenv sjh-resource-manager
workon sjh-resource-manager
pip install -r requirements.txt
```

## Running it all: 
```
./manage.py makemigrations
./manage.py migrate
./manage.py runserver <ip>:<port>
```
