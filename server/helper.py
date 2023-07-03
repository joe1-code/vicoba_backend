from server.models import Users
from functools import wraps
from flask import request, jsonify, g
import jwt
import os
import random
import datetime

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
            g.groupid = data['groupid']
            g.userid = data['id']
            
            

          

        except jwt.ExpiredSignatureError as e:
            return jsonify({'message': 'Token has expired'})
        return f(*args, **kwargs)
    return decorated


# # ................... for admin actions .....add()

# def token_required_admin(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         token = request.headers.get('Authorization')
#         if not token:
#             return jsonify({'message': 'Token is missing'}), 403

#         parts = token.split()
#         if parts[0].lower() != "bearer":
#             return jsonify({"message": "Authorization header must start with Bearer"}, 401)
#         elif len(parts) == 1:
#             return jsonify({"message": "Token not found"}, 401)
#         elif len(parts) > 2:
#             return jsonify({"message": "Invalid header"}, 401)
#         token = parts[1]
#         try:

#             data = jwt.decode(token, os.environ.get(
#                 'SECRET_KEY'), algorithms="HS256")
#         #   add role,branchId to request
#         #   request.data={**request.data,'role':}
#         except jwt.ExpiredSignatureError as e:
#             return jsonify({'message': 'Token has expired'})
#         return f(*args, **kwargs)
#     return decorated


# # >>>>>>><<<<<< ........ check if is doctor ..........



  

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

            data = jwt.decode(token, os.environ.get('SECRET_KEY'), algorithms="HS256")
           
          #add the userid to the global storage cache/object
            g.userid=data['id']
            g.groupid=data['groupid']
          # check if role is admin if not return error present in token
            if not data['role'] =='admin':
                return jsonify({"message": "you are neither an admin!"}, 403)
                
        except jwt.ExpiredSignatureError as e:
            return jsonify({'message': 'Token has expired'}),403

        except jwt.exceptions.InvalidSignatureError as e:
            return jsonify({'message': 'Invalid Token'})
        return f(*args, **kwargs)
    return decorated

#-----------------------------serializer----------------------------------------
def users_serializer(data):
 return {
        "fullname": data.firstname + " " + data.lastname,
        "phoneNo": data.phoneNo,
        "userid": data.userid,
        "role": data.role
        }
            
def apis_serializer(data):
    return{
        "firstname":data.firstname,
        "lastname":data.lastname,
        "userid":data.userid,
        "role":data.role
    }

def window_serializer(data):
    return{
        "groupID": data.groupid
    }

def windview_serializer(data):
    return{
        "startdate":data.startdate.isoformat() if data.startdate else None,
        "receivers":data.receivingpeople
    }

    





# #----------serializer-----------
# def randomGenerator():
#     min = pow(10, int(size)-1)
#     max = pow(10, int(size)) - 1
#     return random.randint(min, max)


# def profile_serializer(data):
#     return {
#         'userid': data.name,
#         'email': data.email,
#         'phone': data.phone
#     }


# def users_serializer(data):

#     return {
#         "userid": data.userid,
#         "fname": data.fname,
#         "lname": data.lname,
#         "email": data.email,
#         "PhoneNo": data.PhoneNo,
#          "role": data.role
#     }

