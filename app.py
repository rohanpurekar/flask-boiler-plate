from flask import Flask
from flask_restful import Resource, Api
from flask_jwt import JWT
from resources.user import UserRegister
from authentication.security import authenticate, identity
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'rohan'
api = Api(app)


jwt = JWT(app, authenticate, identity)
@app.route('/')
def hello():
    return "Bon Voyage with this BoilerPlate"

api.add_resource(UserRegister,'/register')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True, port=5000)