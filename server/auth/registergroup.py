from flask_sqlalchemy import model
from jwt import exceptions
from server.models import Group, Users
import uuid
from flask_session import Session
from flask import jsonify
from werkzeug.security import generate_password_hash


#create group id & adminid
groupId=uuid.uuid4()
adminId=uuid.uuid4()

def registerGroup(data, db):
 groupname=data['groupname']
 totalmembers=data['totalmembers']
 fname=data['firstname']
 lname=data['lastname']
 mobile=data['phoneNo']
 mail=data['email']
 passwd=data['password']
 location=data['place']
 title=data['title']

 

 #check if admin exists
 admin=Users.query.filter_by(phoneNo=mobile).first()

 if not admin:
  try:
   #generate hashed password
   passcode=generate_password_hash(passwd)
   Regadmin=Users(groupid=groupId, userid=adminId, firstname=fname, lastname=lname, phoneNo=mobile, email=mail, password=passcode, place=location, title=title, role='admin')

   #register a group to db
   newgroup=Group(groupid=groupId, adminid=adminId, groupname=groupname, totalmembers=totalmembers)


   db.session.add(newgroup)
   db.session.add(Regadmin)
   db.session.commit()

   return ({'message':'New group registered'}),200
  except Exception as e:
   print(e)
   return ({'message':'failed to register group'}),403

