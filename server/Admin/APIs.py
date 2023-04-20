from flask import jsonify
from server.models import Users

from ..helper import apis_serializer
def fetchUser(Users):
 pages_perpage=100
 pages=1

 userProfile=Users.query.filter_by()

 if userProfile:
  data=[*map(apis_serializer, userProfile)]
  return jsonify({'data':data})
 else:
  return ({'message':'data not found!'})
