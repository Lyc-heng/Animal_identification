from flask_login import UserMixin

from date_base import db


# user models
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    animals = db.Column(db.String(512))
