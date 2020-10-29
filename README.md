# flask_sqlite
A Flask Application that demonstrates people portal and 
SQLite database.

## Instructions
As always ensure you create a virtual environment for this application and install
the necessary libraries from the `requirements.txt` file.

```
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Start the development server

```
$ python run.py
```


Browse to http://0.0.0.0:8080

# People portal
This is a Flask app with perission level access for people portal. 
CRUD opeartion on usertypes. 

1. relational entities:
    1. Admin
    2. Eng Manager
    3. Office manager
2. Admin have all access. Admin: employee_create, 
employee_read, employee_edit , employee_delete,  conf_room_create, conf_room_read, conf_room_edit, conf_room_delete
3. Engg Manager: employee_create, employee_read, employee_edit
4. Office Manager: conf_room_create, conf_room_read, conf_room_edit
5. Default: employee_read, conf_room_read

## Installation and Set Up
Clone the repo from GitHub:
```
git clone https://github.com/sachisabya28/Peopleportal
```

Fetch from the develop branch:
```
git fetch origin develop
```

Navigate to the root folder:
```
cd app
```

Install the required packages:
```
pip install -r requirements.txt
```
```
set ENVIRONMENT= 'option' - this is either production or development
```
```
options
  'development'
  'production'
  'testing'
```  

Initialize, migrate, and upgrade the database for setup
```
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

## Launching the Program
Run ```python run.py```. 



## Web App

The app has a web-based interface and can be accessed [here](/). A sample user has already been created with the following credentials:

```
#admin user login
username: admin@email.com
password: password1
```

```
#Engg Manager user login
username: engmanager@email.com
password: password2
```

```
#office Manager user login
username: ofcmanager@email.com
password: password3
```
