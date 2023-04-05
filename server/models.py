from enum import unique
from .extensions import db
# from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash
#import uuid


#userid = uuid.uuid4()



class Group(db.Model):

    __tablename__='Group'

    id=db.Column(db.Integer, primary_key=True)
    groupid=db.Column(db.String(200), nullable=False, unique=True)
    adminid=db.Column(db.String(200),nullable=False,unique=True)
    groupname=db.Column(db.String(200), nullable=False)

class Users(db.Model):

    __tablename__='Users'

    id=db.Column(db.Integer, primary_key=True)
    userid=db.Column(db.String(200), nullable=False, unique=True)
    firstname=db.Column(db.String(200), nullable=False)
    lastname=db.Column(db.String(200), nullable=False)
    phoneNo=db.Column(db.String(200),nullable=False, unique=True)
    email=db.Column(db.String(200), nullable=False, unique=True)
    password=db.Column(db.String(200), nullable=False)
    place=db.Column(db.String(200),nullable=False)
    title=db.Column(db.String(200),nullable=False)
    code=db.Column(db.String(200), nullable=True)

