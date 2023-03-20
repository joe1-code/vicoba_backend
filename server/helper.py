from server.models import Users
from functools import wraps
from flask import request, jsonify, g
import jwt
import os
import random

size = os.environ.get('TRACKING_ID_SIZE')


# .............. for any user ..........


def token_required_user(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing'}), 403

        parts = token.split()
        if parts[0].lower() != "bearer":
            return jsonify({"message": "Authorization header must start with Bearer"}, 401)
        elif len(parts) == 1:
            return jsonify({"message": "Token not found"}, 401)
        elif len(parts) > 2:
            return jsonify({"message": "Invalid header"}, 401)
        token = parts[1]
        try:

            data = jwt.decode(token, os.environ.get(
                'SECRET_KEY'), algorithms="HS256")

            # add role and userid to flask global storage cache
            print(data)
            g.userRole = data['role']
            g.userid = data['id']
            
            

          

        except jwt.ExpiredSignatureError as e:
            return jsonify({'message': 'Token has expired'})
        return f(*args, **kwargs)
    return decorated


# ................... for admin actions .....add()

def token_required_admin(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing'}), 403

        parts = token.split()
        if parts[0].lower() != "bearer":
            return jsonify({"message": "Authorization header must start with Bearer"}, 401)
        elif len(parts) == 1:
            return jsonify({"message": "Token not found"}, 401)
        elif len(parts) > 2:
            return jsonify({"message": "Invalid header"}, 401)
        token = parts[1]
        try:

            data = jwt.decode(token, os.environ.get(
                'SECRET_KEY'), algorithms="HS256")
        #   add role,branchId to request
        #   request.data={**request.data,'role':}
        except jwt.ExpiredSignatureError as e:
            return jsonify({'message': 'Token has expired'})
        return f(*args, **kwargs)
    return decorated


# >>>>>>><<<<<< ........ check if is doctor ..........


def token_required_doctor(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing'}), 403

        parts = token.split()
        if parts[0].lower() != "bearer":
            return jsonify({"message": "Authorization header must start with Bearer"}, 401)
        elif len(parts) == 1:
            return jsonify({"message": "Token not found"}, 401)
        elif len(parts) > 2:
            return jsonify({"message": "Invalid header"}, 401)
        token = parts[1]
        try:

            data = jwt.decode(token, os.environ.get(
                'SECRET_KEY'), algorithms="HS256")
        
          # check if role is doctor if not return error

            if not data['role'] =='doctor':
                return jsonify({"message": "Permission not granted!"}, 403)
                
        except jwt.ExpiredSignatureError as e:
            return jsonify({'message': 'Token has expired'})
        return f(*args, **kwargs)
    return decorated

#---------------------check if is an Admin---------------------
def token_required_admin(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing'}), 403

        parts = token.split()
        if parts[0].lower() != "bearer":
            return jsonify({"message": "Authorization header must start with Bearer"}, 401)
        elif len(parts) == 1:
            return jsonify({"message": "Token not found"}, 401)
        elif len(parts) > 2:
            return jsonify({"message": "Invalid header"}, 401)
        token = parts[1]
        try:

            data = jwt.decode(token, os.environ.get(
                'SECRET_KEY'), algorithms="HS256")
        
          # check if role is admin if not return error

            if not data['role'] =='Admin':
                return jsonify({"message": "you are neither an admin!"}, 403)
                
        except jwt.ExpiredSignatureError as e:
            return jsonify({'message': 'Token has expired'})
        return f(*args, **kwargs)
    return decorated







#----------serializer-----------
def randomGenerator():
    min = pow(10, int(size)-1)
    max = pow(10, int(size)) - 1
    return random.randint(min, max)


def profile_serializer(data):
    return {
        'userid': data.name,
        'email': data.email,
        'phone': data.phone
    }


def users_serializer(data):

    return {
        "userid": data.userid,
        "fname": data.fname,
        "lname": data.lname,
        "email": data.email,
        "PhoneNo": data.PhoneNo,
         "role": data.role
    }

def appointments_serializer(data):
    if data.patientid:
        patiendata = Users.query.filter_by(userid=data.patientid).first()
        patientname =  patiendata.fname+" "+patiendata.lname
        email =patiendata.email
        phone= patiendata.PhoneNo
    else:
       patientname =  ''
       email =''
       phone= ''


    return {
        "bookingdate": data.bookingdate,
        "status": data.status,
        "patientid": data.patientid,
        "patientname": patientname,
        "email":email,
        "phone":phone
    }






