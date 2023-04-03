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
  # token = Users.query.with_entities(Users.code).filter_by(phoneNo=mobilenumber).first()
  token=Users.query.filter_by(phoneNo=mobile).first()
  newToken=(f"{token.code}")

  if token:
   newToken=(f"{token.code}")
   # print (newToken)
   # print(usercode)
   #decrypt the token for comparison with usercode
   print("test")
   try:
    # decoded = jwt.decode(newToken, 'SECRET_KEY', algorithms=['HS256'])
    payload = jwt.decode(newToken, os.environ.get('SECRET_KEY'), algorithms=['HS256'])
    print(payload)
    return ({'decrypted':payload})
   except Exception as e:
    print(e)
    return ({'message':'failed to decrypt'})

   return (newToken)

  
  print(newToken)
  # newtoken=bytes(token, 'utf-8')
  
  return {}