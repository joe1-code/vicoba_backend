from flask_sqlalchemy import model
import uuid
from server.models import Users,Newwindow
from flask_session import Session
from flask import jsonify

#create a windowid
windId=uuid.uuid4()

def Registerwindow(data, db, Users):
 
 #accept data from the UI
 startdate=data['startdate']
 amount=data['payamount']
 duration1=data['durationOne']
 receiver=data['receivingpeople']
 total=data['total']
 duration2=data['durationTwo']
 participatorsId=data['participators']

 #fetching the first element from an array
 element = participatorsId[0]

 #querying a group id from db
 Info = Users.query.filter_by(userid = element).first()
 groupID = Info.groupid
 print("group id:", groupID)




 #post data to db
 try:
  newwind=Newwindow(windowid=windId, startdate=startdate,payamount=amount, durationOne=duration1,durationTwo=duration2, receivingpeople=receiver, total=total, groupid=groupID)

  for userid in participatorsId:
   updatewindowid = Users.query.filter_by(userid=userid).first()
   updatewindowid.windowid=windId
   db.session.add(updatewindowid)
   db.session.commit()
  
  db.session.add(newwind)
  db.session.commit()

  
  return ({'message':'new window registered'}),200

 except Exception as e:
  print(e)

  return ({'message':'did not register window'}),403

