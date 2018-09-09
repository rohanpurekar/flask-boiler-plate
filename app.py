from flask import Flask
from flask_restful import Resource, Api
from flask_jwt import JWT
from flask_admin import Admin
from resources.user import UserRegister
from authentication.security import authenticate, identity
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'rohan'
api = Api(app)
admin = Admin(app)


jwt = JWT(app, authenticate, identity)

@app.route('/')
def hello():
    return "Bon Voyage with this BoilerPlate"

api.add_resource(UserRegister,'/register')


if __name__ == '__main__':
    from db import db
    from flask_admin.contrib.sqla import ModelView
    from models.user import UserModel

    db.init_app(app)
    admin.add_view(ModelView(UserModel, db.session))
    app.run()