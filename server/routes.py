from flask import Blueprint, request, jsonify, g
from .extensions import db
from server.auth.register import register
from server.auth.login import login
from server.auth.forgotpass import forgotPassword
from server.auth.resetpass import resetPassword
from server.models import Users


from flask_cors import CORS, cross_origin

main=Blueprint('main', __name__)
CORS(main, support_credentials=True)


# ---------- Authentication routes ----------
@main.route('/register', methods=['POST', 'OPTIONS'])
@cross_origin(support_credentials=True)
def Reguser():
 if(request.method=='POST'):
  data=request.json
  return register(data, db)
 else:
  pass

@main.route('/login', methods=['POST', 'OPTIONS'])
@cross_origin(support_credentials=True)
def Userlogin():
 if(request.method=='POST'):
  return login(request, Users)
 else:
  pass

@main.route('/forgotpass', methods=['POST', 'OPTIONS'])
@cross_origin(support_credentials=True)
def Forgotpass():
  if(request.method=='POST'):
    return forgotPassword(request, Users, db)
  else:
    pass

@main.route('/resetpass', methods=['POST', 'OPTIONS'])
@cross_origin(support_credentials=True)
def Resetpass():
  if(request.method=='POST'):
    return resetPassword(request, Users, db)
  else:
    pass


