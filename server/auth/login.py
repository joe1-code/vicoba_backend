import jwt
import os
import json
from datetime import datetime,timedelta
from flask import jsonify
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token,create_refresh_token

def login(request, Users):
 #verify the posted data
 data=json.loads(request.data)
 if data:
  username=data['phoneNo']
  password=data['password']
  print(username, password)

  #check if user exists
  exist_user=Users.query.filter_by(phoneNo=username).first()

  if not exist_user or not check_password_hash(exist_user.password, password):
   return jsonify({'message':'wrong credentials'}),401

  #create token for the user

  token=jwt.encode({'id':exist_user.userid, 'exp':datetime.utcnow() + timedelta(seconds=int(os.environ.get(
   'DURATION'), base=0)), 'role':exist_user.role}, os.environ.get('SECRET_KEY'))

  return jsonify({'token':token}),200

 return jsonify({'message':'authorization is missing'}),403