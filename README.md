# Flask Boilerplate

A boilerplate repository to jump start flask projects.

## Getting Started
It is advisable to clone this flask repository inisde a virtual environment.
The database used is PostgreSQL. SQLAlchemy is used to perform database operations.
The database URL has to be set as an environment variable as the code fetches this
variable. This is beneficial since during the deployment on Heroku, it fetches the
same variable.

```
SET [DATABASE_URL] = export DATABASE_URL="postgresql://localhost/<db name>"
SET [DEV_ENV] = export FLASK_ENV='development'
```
I will be adding the detailed description soon



## Authors

* **Rohan Purekar** - *Initial work* - [Rohan Purekar](https://github.com/rap999a)

See also the list of [contributors](https://github.com/rap999a/flask-boiler-plate/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


