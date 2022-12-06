from __init__ import db
from flask_login import UserMixin
from sqlalchemy.sql import func


# class Transport(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     location = db.Column(db.String(1000))
#     destination = db.Column(db.String(1000))
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.String(15), nullable=False, primary_key=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)
    status = db.Column(db.Boolean, default=1)