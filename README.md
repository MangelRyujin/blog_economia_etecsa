# blog_economia_etecsa

## Previous knowledge
<!-- UL -->
1. [Git](https://github.com/)
2. [Python](https://www.python.org/)
3. [Django](https://www.djangoproject.com/)

## Getting started

Follow the steps below to install the app in your corresponding environment

## Download the repository via git

```
# Clone git repo in your path
git clone https://github.com/MangelRyujin/blog_economia_etecsa.git
      
```

## Development environment 

Create your virtual env 

```
Example:
python -m venv env    
```
Linux Run env
```
source env/bin/activate
```

Windows Run env
```
env\Scripts\activate
```


## Install the project requirements

>Run next comand 
```
pip install -r requirements.txt
```

## Run migrations

```python
python manage.py migrate
```

## If you want to create a super user
##### Remember to enter real emails so that the task editing messages can reach multiple users.

```python
python manage.py createsuperuser
```


## Run server

```python
python manage.py runserver
```