from app import app, admin
from db import db
from flask_admin.contrib.sqla import ModelView
from models.user import UserModel


db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

admin.add_view(ModelView(UserModel, db.session))
