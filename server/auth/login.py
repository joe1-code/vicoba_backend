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

  #check if user exists
  exist_user=Users.query.filter_by(phoneNo=username).first()

  if not exist_user or not check_password_hash(exist_user.password, password):
   return jsonify({'message':'wrong credentials'}),401

  #create token for the user
  duration=int(os.environ.get('DURATION1',360))
  expiration_time = datetime.utcnow() + timedelta(seconds=duration)
  payload={'id':exist_user.userid, 'role':exist_user.role, 'groupid':exist_user.groupid}
  token = jwt.encode({'exp': expiration_time, **payload}, os.environ.get('SECRET_KEY'), algorithm='HS256')

  
  return jsonify({'token':token}),200

 return jsonify({'message':'authorization is missing'}),403