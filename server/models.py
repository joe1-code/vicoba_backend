from enum import unique
from sqlalchemy import null
from .extensions import db
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash
#import uuid


#userid = uuid.uuid4()



class RegisterGroup(db.Model):
    __tablename__='RegisterGroups'

    id=db.Column(db.Integer, primary_key=True)
    groupid=db.Column(db.String(200), nullable=False, unique=True)
    groupname=db.Column(db.String(200), nullable=False)
    adminname=db.Column(db.String(200), nullable=False)
    mobile=db.Column(db.Integer, nullable=False, unique=True)
    password=db.Column(db.String(200), nullable=False)
    

class Register(db.Model):
    __tablename__='test'

    id=db.Column(db.Integer, primary_key=True)
    groupid=db.Column(db.String(200), nullable=False, unique=True)
    groupname=db.Column(db.String(200), nullable=False)
   