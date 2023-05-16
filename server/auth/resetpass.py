from server.models import Users
import json
from flask import jsonify
from flask_jwt_extended import create_access_token,create_refresh_token
import os
import jwt
from werkzeug.security import generate_password_hash
from flask_session import Session



def export_data(mobile):
 phone=(f'mobile:{mobile}')
#  print(phone)


def resetPassword(request, Users, db):
 data=json.loads(request.data)
 if data:
  #data from UI
  mobile=data['phoneNo']
  user_code=data['userCode']
  userpassword=data['password']
  
  #convert usercode from string datatype to integer datatype
  usercode=int(user_code)

  #encrypt the password before updating the db
  newpassword=generate_password_hash(userpassword)

  #fetching encryted token from db
  token=Users.query.filter_by(phoneNo=mobile).first()
  newToken=(f"{token.code}")

  if token:
   newToken=(f"{token.code}")
   
   #decrypt the token for comparison with usercode
   try:
    auth_token = jwt.decode(newToken, os.environ.get('SECRET_KEY'), algorithms=['HS256'])
    db_code=(auth_token['code'])
    expireTime=(auth_token['exp'])

    # return ({'payload':expireTime})

   except Exception as e:
    print(e)
    return ({'message':'failed to decrypt'})

   #Check the datatype of the two codes to prevent comparatory errors
  #  print(type(db_code))
  #  print(type(usercode))

   #compare verification codes
   if usercode==db_code:
   
    #update the password
    user=Users.query.filter_by(phoneNo=mobile).first()
    # print(userpassword)
    # print(newpassword)

    user.password=newpassword
    db.session.add(user)
    db.session.commit()
    return jsonify({'message':' successfully updated password','isSuccessful':True}),200
   else:
    return jsonify({'message':'invalid code'}),401



  
  
  return {}