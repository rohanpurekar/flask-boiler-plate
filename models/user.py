from db import db
from argon2 import PasswordHasher

ph = PasswordHasher()


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    username = db.Column(db.String(80))
    password = db.Column(db.String(160))
    dob = db.Column(db.String(80))

    def __init__(self, first_name, last_name, username, password, dob):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = ph.hash(password)
        self.password = dob

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

