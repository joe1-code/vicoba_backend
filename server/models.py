from enum import unique
from sqlalchemy import null
from .extensions import db
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash
#import uuid


#userid = uuid.uuid4()


class Users(db.Model):

    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.String(200), nullable=False, unique=True)
    fname = db.Column(db.String(200), nullable=False)
    lname = db.Column(db.String(200), nullable=False)
    role=db.Column(db.String(200),nullable=False)
    email=db.Column(db.String(200),nullable=False,unique=True)
    password=db.Column(db.String(200),nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    updated = db.Column(db.DateTime, default=datetime.utcnow)
    PhoneNo=db.Column(db.Integer,nullable=False,unique=True)

