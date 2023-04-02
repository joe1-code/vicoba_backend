from server.models import Users
import json
from flask import jsonify
from flask_jwt_extended import create_access_token,create_refresh_token
import os
import jwt


def export_data(mobile):
 phone=(f'mobile:{mobile}')
 return jsonify({'mobile':phone})
# phone={}
# def export_data(mobile):
#  global phone
#  phone={'phone':mobile}
#  return phone

def resetPassword(request, Users):
 data=json.loads(request.data)
 if data:
  #data from UI
  # mobile=data['phoneNo']
  usercode=data['code']
  newpassword=['password']
  # print(mobile)
  #fetching encryted token from db
  token = Users.query.with_entities(Users.code).filter_by(phoneNo=mobilenumber).first()
  print("code:",token)
  #decrypt the token for comparison with usercode
  # newtoken=bytes(token, 'utf-8')
  # try:
  #  # decoded = jwt.decode(newtoken, 'secret_key', algorithms=['HS256'])
  #  return ({'decrypted':decoded})
  # except Exception as e:
  #  print(e)
  #  return ({'message':'failed to decrypt'})
  return {}