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

  
  #check the user if exists
  exist_user=Users.query.filter_by(phoneNo=mobile).first()
  if not exist_user:
   return jsonify({'message':'not a user'})


  #Generate code
  code=random.randint(1000,9999)
  

  #Get the token lasting duration from the env. file
  duration=int(os.environ.get('DURATION1',360))
  expiration_time = datetime.utcnow() + timedelta(seconds=duration)
  payload={'id':exist_user.userid, 'code':code}
  codetoken = jwt.encode({'exp': expiration_time, **payload}, os.environ.get('SECRET_KEY'), algorithm='HS256')

  #post the code to db
  exist_user.code=codetoken
  db.session.add(exist_user)
  db.session.commit()
  
  #import the module function that you will export the mobile data
  from server.auth.resetpass import export_data
 
  # Pass the form data to the export_data function
  export_data(mobile)

  return jsonify({'message':code})

