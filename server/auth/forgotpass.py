import os
import random
from flask import jsonify
import json

def resetPassword(request, Users):

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
  return jsonify({'message':code})
