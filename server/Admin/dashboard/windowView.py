from flask import jsonify,g
import json


from server.helper import window_serializer, windview_serializer

def windowView(Users, Newwindow):
 pages_perpage=100
 page = 1

 userID = g.userid
 profile = Users.query.filter_by(userid = userID)
 if profile:
  # create empty array to store an obj value
  raw_values = []

  data = [*map(window_serializer, profile)]

  # iterate through a list object
  for value in data:
   raw_value=value["groupID"]
   raw_values.append(raw_value)
   
   raw_Data = raw_values[0] 

  # querying the startdate from Newwindow table using groupID
  windData = Newwindow.query.filter_by(groupid = raw_Data)
  # print("no data",windData)
  if windData:
   output = [*map(windview_serializer, windData)]
  
   print("data from db",output)

  return {"data":output}
 

 else:
  print({"message":"data not found!"}),403

 
 #  data = profile.groupid
 #  print("typooooooooooooo", data)


 # windData = Newwindow.query.filter_by(groupid = data).first()
 # print(windData)
 # if windData:
 #  startdate = windData.startdate
 #  print("startCycle",startdate)

 # return ({'message':windData})
 
 

