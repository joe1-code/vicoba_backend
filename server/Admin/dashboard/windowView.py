from flask import jsonify,g
import json


from server.helper import window_serializer

def windowView(Users):
 pages_perpage=100
 page = 1

 print("The user id from the token",g.userid)
 userID = g.userid
 profile = Users.query.filter_by(userid = userID)

 if profile:
  data = [*map(window_serializer, profile)]
  return {"data":data}

 else:
  abort(403,"data not found!")