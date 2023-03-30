from flask import Blueprint, request, jsonify, g
from .extensions import db
from server.auth.register import register


from flask_cors import CORS, cross_origin

main=Blueprint('main', __name__)
CORS(main, support_credentials=True)


# ---------- Authentication routes ----------
@main.route('/register', methods=['POST', 'OPTIONS'])
@cross_origin(support_credentials=True)
def Reguser():
 print('check out',request)
 if(request.method=='POST'):
  data=request.json
  return register(data, db)
 else:
  pass



