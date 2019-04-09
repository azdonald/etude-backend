import uuid
import datetime

from main.models import db 
import main.services.tokenService as ts
import main.models.schoolModels as sm
import main.schemas.courseSchema as cs

def getAllCourses():
    courses = sm.Course.query.all()

def getCourse(courseId):
    course = sm.Course.query.filter_by(publicId=courseId).first()
    schema = cs.CourseSchema()
    return schema.dump(course)