from flask_restful import Resource
from flask import request, jsonify
from flask_jwt_extended import  jwt_required

from main.services.userService import *
from main.services.tokenService import getUserDetails



class UserRegistration(Resource):
    def post(self):
        result, status = save_user(request.get_json())
        return result, status


class UserLogin(Resource):
    def post(self):
        result, status = authenticateUsers(request.get_json())
        return result, status

class UserProfile(Resource):
    @jwt_required
    def get(self):
        currentUser = getUserDetails()
        user = getUser(currentUser['id'])
        return user

class TutorProfile(Resource):
    @jwt_required
    def post(self):
        currentUser = getUserDetails()
        result, status = save_tutor_profile(request.get_json(), currentUser['id'])
        return result, status

    @jwt_required
    def get(self):
        currentUser = getUserDetails()
        result, status = getTutorProfile(currentUser['id'])
        return result, status

class StudentProfile(Resource):
    @jwt_required
    def post(self):
        currentUser = getUserDetails()
    