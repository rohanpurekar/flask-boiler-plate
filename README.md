# Flask Boilerplate

A boilerplate repository to jump start flask projects. Just clone it
to start a project with JWT Authentication, PostgreSQL database
connectivity, admin panel and sample template for the UI. The repo
is Heroku config ready.

## Boilerplate Features
* **SQLAlchemy-Postgres Database**
* **Sample User Model**
* **JWT Authentication**
* **Heroku Deployment Ready Config**
* **Argon2 Cffi Password Hashing**

## Getting Started
It is advisable to clone this flask repository inisde a virtual environment.
The database used is PostgreSQL. 

```
    python -m venv <environment name>
```
SQLAlchemy is used to perform database operations.
The database URL has to be set as an environment variable as the code fetches this
variable from the virtual environment. This is beneficial since during the deployment 
on Heroku, it fetches the same variable. Set the flask environment as development.


```
    SET [DATABASE_URL] = export DATABASE_URL="postgresql://localhost/<db name>"
    SET [DEV_ENV] = export FLASK_ENV='development'
```
The dependencies are stored in requirements.txt file. In the root
directory run the following command to install the dependencies. 
```
    pip install
```
The data models need to be migrated for changes to be made to the 
database like Django. The psycopg2 package is used to work with
PostgreSQL. The Alembic package which is a part of Flask-Migrate
 is used to make migrations.
 
 ```
     python manage.py db init
 ```
 This command will create the migrations and a new folder called
  migrations will be created in the root directory. There will 
  also be a directory called versions which will store all the
   migrations.
 
 ```
     python manage.py db migrate
 ```
This command will generate the migration files in the versions
 directory.
 
 ```
     python manage.py db upgrade
 ```
This command will be responsible for applying the changes to the
database.

### Authentication
Flask-JWT package is used for JWT token based authentication.
 On the api the username as password are sent. The user details
  are validated and a token is sent on successful authentication. The url
 for authentication is provided by the package itself. Remember,
 the port number is based on what is given in the app.py file by you.
 
 ```
     http://127.0.0.1:5000/auth
 ```
### Flask Admin Panel
```
    Coming soon
```   


### Templates
```
    Coming soon
``` 

## Authors

* **Rohan Purekar** - *Initial work* - [Rohan Purekar](https://github.com/rap999a)

See also the list of [contributors](https://github.com/rap999a/flask-boiler-plate/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


