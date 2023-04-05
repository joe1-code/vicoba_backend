from flask_sqlalchemy import model
from jwt import exceptions
from server.models import Group
import uuid
from flask_session import Session
from flask import jsonify
from werkzeug.security import generate_password_hash


#create group id & adminid
groupid=uuid.uuid4()
adminid=uuid.uuid4()

def registerGroup(data, db):
 groupname=data['groupname']