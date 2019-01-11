import uuid
import datetime

from main.models import db 
import main.services.tokenService as ts
import main.models.userModels as um 
import main.schemas.userSchema as us



def save_user(data):
    user = um.User.query.filter_by(email=data['email']).first()
    if not user:
        user = um.User(firstname=data['firstname'], lastname=data['lastname'],
                        email=data['email'], password=data['password'],
                        publicid=str(uuid.uuid4()), user_type=um.UserType(data['user_type']))
        
        save_changes(user)
        token = ts.generateToken(user.asDict())
        return token, 201
    else:
        response = {
            'status': 'error',
            'message': 'User already exists'
        }
        return response, 403

def save_tutor_profile(data, userId):
    tutor = um.TutorProfile.query.filter_by(user_id=userId).first()
    if not tutor:
        tutor = um.TutorProfile(bio=data['bio'], rate=data['rate'], user_id=userId)
    else:
        if 'bio' in data:
            tutor.bio = data['bio']
        if 'rate' in data:
            tutor.rate = data['rate']
    save_changes(tutor)
    schema = us.TutorProfileSchema()
    profile = schema.dump(tutor)
    return profile, 201

def getAllUsers():
    users = um.User.query.all()

def getUser(userId):
    user = um.User.query.filter_by(id=userId).first()
    schema = us.UserSchema()
    return schema.dump(user)

def getTutorProfile(userId):
    tutor = um.TutorProfile.query.filter_by(user_id=userId).first()
    if tutor is None:
        response = {
            'status': 'error',
            'message': 'Tutor not found'
        }
        return response, 404
    schema = us.TutorProfileSchema()
    profile = schema.dump(tutor)
    return profile, 200

def authenticateUsers(data):
    user = um.User.query.filter_by(email=data['email']).first()
    response = {
            'status': 'error',
            'message': 'Invalid credentials'
        }
    if not user:
        return response, 200
    else:
        auth = user.checkPassword(data['password'])
        if auth:
            token = ts.generateToken(user.asDict())
            return token, 200
        else:
            return response, 200

def save_changes(data):
    db.session.add(data)
    db.session.flush()
    db.session.commit()
