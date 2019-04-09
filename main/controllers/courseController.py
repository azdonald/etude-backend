from flask_restful import Resource
from flask import request, jsonify
from flask_jwt_extended import  jwt_required

from main.services.courseService import *
from main.services.tokenService import getUserDetails


class Courses(Resource):
    def get(self):
        courses = getAllCourses()
        return courses