from flask import Blueprint, request, jsonify, g
from .extensions import db
from .models import Users,Appointment
# from .auth.login import login
# from .auth.reset import resetPassword
# from .doctorprofile.profile import createprofile
# from .patient.finddoctors import doctors
# from .auth.register import register
# from .patient.Addbooking import addappointment
# from .doctorprofile.viewappointment import getappointment
# from .Admin.patientdelete import removeUser
# from .Admin.users import users
# from .profile.userRole import getUserbyrole
from .helper import token_required_user, token_required_admin,token_required_doctor
# from .profile.userProfile import profile
from flask_cors import CORS, cross_origin



main = Blueprint('main', __name__)
CORS(main, support_credentials=True)


# ---------- Authentication routes ----------




@main.route('/login', methods=['POST', 'OPTIONS'])
@cross_origin(supports_credentials=True)
def Userlogin():
    if(request.method == 'POST'):
        return login(request, Users)
    else:
        pass



# ---------- Admin actions ---------------------------


    

