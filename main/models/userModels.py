import enum
import datetime
import uuid
from . import db, bcrypt


class UserType(enum.IntEnum):
    ADMIN=1
    TUTOR=2
    STUDENT=3

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    firstname = db.Column(db.String(255), nullable=False)
    lastname = db.Column(db.String(255), nullable=False)
    password_hash = db.Column(db.String(100))
    publicid = db.Column(db.String(100), unique=True)
    user_type = db.Column(db.Enum(UserType))
    created_on = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    updated_on = db.Column(db.DateTime, onupdate=datetime.datetime.utcnow())

    @property
    def password(self):
        raise AttributeError('Write only field')
    
    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def checkPassword(self, password):
        return bcrypt.check_password_hash(self.password_hash, password);

    def asDict(self):
        return {'id':self.id, 'publicid':self.publicid, 'user_type':self.user_type, 'firstname':self.firstname}


    def __repr__(self):
        return "<User '{} {} {}' ".format(self.firstname, self.lastname, self.id)

class TutorProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    bio = db.Column(db.String(255))
    rate = db.Column(db.Numeric(10,2))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('users', lazy=True))
    created_on = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    updated_on = db.Column(db.DateTime, onupdate=datetime.datetime.utcnow())


class StudentProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    bio = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('student_users', lazy=True))
    created_on = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    updated_on = db.Column(db.DateTime, onupdate=datetime.datetime.utcnow())




#Represents a many to many relationship 
tutor_courses = db.Table('tutor_courses',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('course_id', db.Integer, db.ForeignKey('course.id'), primary_key=True)
)

