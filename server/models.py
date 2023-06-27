from enum import unique
from .extensions import db
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash





class Group(db.Model):

    __tablename__='Group'

    id=db.Column(db.Integer, primary_key=True)
    groupid=db.Column(db.String(200), nullable=False, unique=True)
    adminid=db.Column(db.String(200),nullable=False,unique=True)
    groupname=db.Column(db.String(200), nullable=False)
    totalmembers=db.Column(db.String(200), nullable=False)

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
    title=db.Column(db.String(200),nullable=True)
    role=db.Column(db.String(100), nullable=True)
    code=db.Column(db.String(200), nullable=True)
    groupid=db.Column(db.String(200), nullable=True)
    windowid=db.Column(db.String(200), nullable=True)

class Newwindow(db.Model):
    
    __tablename__='Newwindow'

    id=db.Column(db.Integer, primary_key=True)
    windowid=db.Column(db.String(200),nullable=False)
    startdate=db.Column(db.DateTime, default=datetime.utcnow)
    payamount=db.Column(db.String(200), nullable=False)
    durationOne=db.Column(db.String(200), nullable=True)
    receivingpeople=db.Column(db.String(200), nullable=False)
    total=db.Column(db.String(200), nullable=True)
    durationTwo=db.Column(db.String(200), nullable=True)
    groupid=db.Column(db.String(200),nullable=True)