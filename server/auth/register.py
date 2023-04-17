from flask_sqlalchemy import model
from server.models import Users
from flask_session import Session
from flask import jsonify
import uuid
from werkzeug.security import generate_password_hash

#create user id
userid=uuid.uuid4()

def register(data, db):

 fname=data['firstname']
 lname=data['lastname']
 mobile=data['phoneNo']
 mail=data['email']
 passwd=data['password']
 location=data['place']
 title=data['title']

 #check if user exists
 existuser=Users.query.filter_by(phoneNo=mobile).first()
 if not existuser:
  try:
   passcode=generate_password_hash(passwd)
   newuser=Users(userid=userid, firstname=fname, lastname=lname, phoneNo=mobile,   email=mail, password=passcode, place=location, title=title, role='user')
   db.session.add(newuser)
   db.session.commit()
   return jsonify({'message':'user registered successfully'}),200
  except Exception as e :
   print('Error from db',e)
   return jsonify({'message':'registration failed!'}),403
   pass
 return jsonify({'message':'user already exists'}), 409

