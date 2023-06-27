from flask import jsonify,g
import json


from server.helper import window_serializer

def windowView(Users, Newwindow):
 pages_perpage=100
 page = 1

 userID = g.userid
 profile = Users.query.filter_by(userid = userID).first()
 if profile:
 
  data = profile.windowid
  print("typooooooooooooo", data)


 windData = Newwindow.query.filter_by(windowid = data).first()
 print(windData)
 if windData:
  startdate = windData.startdate
  print("startCycle",startdate)

 return ({})
 #  data = [*map(window_serializer, profile)]

  
 #  return {"data":data}

 # else:
 #  print({"message":"data not found!"}),403

 

