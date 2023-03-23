from enum import unique
from .extensions import db
# from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash
#import uuid


#userid = uuid.uuid4()



class Users(db.Model):

    id=db.Column(db.Integer, primary_key=True)
    groupid=db.Column(db.String(200), nullable=False, unique=True)
    groupname=db.Column(db.String(200), nullable=False)
    adminname=db.Column(db.String(200), nullable=False)
    # mobile=db.Column(db.Integer, nullable=False, unique=True)
    # password=db.Column(db.String(200), nullable=False)
    
