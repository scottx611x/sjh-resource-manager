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
pip install awscli
pip install -r requirements.txt
```

## Running it all: 
```
aws configure
./manage.py makemigrations
./manage.py migrate
./manage.py loaddata resource_manager/fixtures/superuser.json
./manage.py runserver <ip>:<port>
```

## API:
```
# Populate JupyterNode model with your N EC2 instances ids and private ips

PUT http://<ip>:<port>/resource_manager/jupyter_users/scott@scott.com/?volume=/cool/path/to/scotts/volume/
  creates a JupyterUser <scott@scott.com>, creates a new EBS Volume and assocites its id with said user, and checks for the "Fullest" Jupyter EC2 Node and associates it with the JupyterUser
  ```
