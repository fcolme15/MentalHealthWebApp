#here is all the sql tables
from . import db #from this package import sqlalchemy
from flask_login import UserMixin
from sqlalchemy.sql import func

# class Note(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     data = db.Column(db.String(10000))
#     date = db.Column(db.DateTime(timezone=True), default=func.now()) ##just grabs the date and time when this account was created 
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #the type of the col is an id and this foreignkey must be one user.id and it must be valid
    
#if need more tables just do more class whatever()

class User(db.Model, UserMixin): #THE TABLE!!!!
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(9), unique = True)
    password = db.Column(db.String(9))
    ######## notes = db.relationship('Note')#tells flask and sql add a note the note id. Its a list of all notes
        
