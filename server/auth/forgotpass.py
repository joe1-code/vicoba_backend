import os
import random
import jwt
from datetime import datetime,timedelta
from flask import jsonify
import json
from flask_session import Session
from server.models import Users
# from flask_sqlalchemy import model
from flask_jwt_extended import create_access_token,create_refresh_token



def forgotPassword(request, Users, db):

 data=json.loads(request.data)

 if data:
  mobile=data['phoneNo']
  print(mobile)

  #check the user if exists
  exist_user=Users.query.filter_by(phoneNo=mobile).first()
  if not exist_user:
   return jsonify({'message':'not a user'})
   
  #Generate code
  code=random.randint(1000,9999)
  
  #tokenlize the code
  codetoken=jwt.encode({'id':exist_user.userid, 'exp':datetime.utcnow() + timedelta(seconds=int(os.environ.get('DURATION1'), base=0)), 'place':exist_user.place}, os.environ.get('SECRET_KEY'))
  

  #post the code to db
  exist_user.code=codetoken
  db.session.add(exist_user)
  db.session.commit()

  return jsonify({'message':code})

