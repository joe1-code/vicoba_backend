from flask import jsonify, g
import json 

from ..helper import users_serializer
def getUsers(Users):
 pages_perpage=100
 page=1
 
 groupId=g.groupid
 print(groupId)
 
 profile=Users.query.filter_by(groupid=groupId)
 
 if profile:
  data=[*map(users_serializer, profile)]
  return {'data':data}
 else:
  return ({'message':'users not found!'}),403