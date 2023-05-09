from flask import Blueprint, request, jsonify, g
from .extensions import db
from server.auth.register import register
from server.auth.login import login
from server.auth.forgotpass import forgotPassword
from server.auth.resetpass import resetPassword
from server.auth.registergroup import registerGroup
from server.Admin.dashboard.newwindow import Registerwindow
from server.Admin.users import getUsers
from server.Admin.APIs import fetchUser
from server.models import Users
from server.helper import token_required_admin

from flask_cors import CORS, cross_origin


main=Blueprint('main', __name__)
CORS(main, support_credentials=True)


# ---------- Authentication routes ----------
@main.route('/registerUser', methods=['POST', 'OPTIONS'])
@cross_origin(support_credentials=True)
@token_required_admin
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

@main.route('/registerGroup', methods=['POST', 'OPTIONS'])
@cross_origin(support_credentials=True)
def Reggroup():
  if(request.method=='POST'):
    data=request.json
    return registerGroup(data, db)
  else:
    pass

@main.route('/newwindow', methods=['POST', 'OPTIONS'])
@cross_origin(support_credentials=True)
@token_required_admin
def Regwindow():
  if(request.method=='POST'):
    data=request.json
    return Registerwindow(data, db)
  else:
    pass

#------------------getUsers---------------------------------------------------
@main.route('/getUsers', methods=['GET', 'OPTIONS'])
@cross_origin(support_credentials=True)
@token_required_admin
def FetchUsers():
  if(request.method=='GET'):
    return getUsers(Users)
  else:
    pass

@main.route('/apis', methods=['GET', 'OPTIONS'])
@cross_origin(support_credentials=True)
def Getdata():
  if(request.method=='GET'):
    return fetchUser(Users)
  else:
    pass



  