from server.models import Users
import json
from flask import jsonify
from flask_jwt_extended import create_access_token,create_refresh_token
import os
import jwt

def export_data(mobile):
 phone=(f'mobile:{mobile}')
 print(phone)


def resetPassword(request, Users):
 data=json.loads(request.data)
 if data:
  #data from UI
  mobile=data['phoneNo']
  usercode=data['code']
  newpassword=['password']
  #fetching encryted token from db
  token=Users.query.filter_by(phoneNo=mobile).first()
  newToken=(f"{token.code}")

  if token:
   newToken=(f"{token.code}")
   
   #decrypt the token for comparison with usercode
   try:
    # decoded = jwt.decode(newToken, 'SECRET_KEY', algorithms=['HS256'])
    auth_token = jwt.decode(newToken, os.environ.get('SECRET_KEY'), algorithms=['HS256'])
    db_code=(auth_token['code'])
    expireTime=(auth_token['exp'])

    # return ({'payload':expireTime})

   except Exception as e:
    print(e)
    return ({'message':'failed to decrypt'})

   
   #compare verification codes
   if usercode==db_code:
    return jsonify({'message':'verification successfully'}),200
   else:
    return jsonify({'message':'invalid code'}),401


  
  
  return {}