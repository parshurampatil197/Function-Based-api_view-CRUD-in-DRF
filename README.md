

## Simple_Django_CRUD_api using @api_view decorator

![gif](https://developers.giphy.com/branch/master/static/api-512d36c09662682717108a38bbb5c57d.gif)


# Description

I have created Python3/Django CRUD with PostgreSQL that uses Django Rest Framework for building Rest 
Apis. DRF allows us to work with regular function based views.
I have implementd Django function based view for the Restful Web service. We also make use of the @api_view decorator.


## Requirements

Last tested successfully with Python 3.6.19 and Ubuntu 16.04
Django==2.2\
djangorestframework==3.10.2\
psycopg2==2.9.3

[Django](https://www.djangoproject.com/): The web framework for perfectionists with deadlines (Django builds better web apps with less code).

[DRF](https://github.com/gitgik/django-rest-api/blob/master/www.django-rest-framework.org): A powerful and flexible toolkit for building Web APIs


## Quick Setup

1. Create a folder for your project on your local machine
```bash
  mkdir myproject; 
  cd myproject

```

2. Create a virtual environment and install django

```bash
  virtualenv venv --python=python3 ; 
  source venv/bin/activate; 

```

Install the dependencies needed to run the app:
```bash
  pip install -r requirements. txt 

```

3. Download this project template from GitHub
```bash
  git clone https://github.com/parshurampatil197/Simple_Django_CRUD_api.git
  cd Simple_Django_CRUD_api

```

4. Initialize the database

```bash
  python manage.py makemigrations
  python manage.py migrate

```


Run the project

```bash
  python manage.py runserver

```






## API Reference
 
Test API by Using POSTMAN
#### Http request: POST 

```http
  http://127.0.0.1:8000/v1/create/
```

#### Request

```http
 {
    "category" : "Electronics",
    "subcategory" : "Mobile",
    "name": "iphone 12",
    "amount": 40000
    
}
```
#### Http request: GET 

```http
  http://127.0.0.1:8000/v1/all/
```

```http
  http://127.0.0.1:8000/v1/all/?id=1
```

```http
  http://127.0.0.1:8000/v1/all/?category=Electronics
```

#### Response

```http
 {
    "category" : "Electronics",
    "subcategory" : "Mobile",
    "name": "iphone 12",
    "amount": 40000
    
}
```

<<<<<<< HEAD
#### Http request: PUT 

```http
  http://127.0.0.1:8000/v1/update/2
```

#### Http request: DELETE 

```http
  http://127.0.0.1:8000/v1/delete/3
```

=======
>>>>>>> feb95fd495f7aed41aedaff1a7fbd8aae7cf427f

## Authors

- [@parshuram](https://github.com/parshurampatil197)

