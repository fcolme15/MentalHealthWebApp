#here is all the sql tables
from . import db #from this package import sqlalchemy
from flask_login import UserMixin
from sqlalchemy.sql import func

#if need more tables just do more class whatever()
#each class is a table in the models.py

    
class UserLogin(db.Model, UserMixin): #stores information for a profile
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(9), unique = True)
    password = db.Column(db.String(9))
    user_profiles = db.relationship('UserProfile')

class UserProfile(db.Model):
    user_profile_id = db.Column(db.Integer, primary_key = True, unique = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_login.user_id'), nullable = False)
    num_flowers = db.Column(db.Integer)
    flower_status = db.Column(db.Boolean)
    carryover = db.Column(db.Boolean)
