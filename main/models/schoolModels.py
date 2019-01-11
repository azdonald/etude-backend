from . import db
import datetime

class School(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), unique=True)
    alias = db.Column(db.String(100))
    created_on = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    updated_on = db.Column(db.DateTime, onupdate=datetime.datetime.utcnow())

    def __repr__(self):
        return "<School '{}' ".format(self.name)


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    code = db.Column(db.String(50), nullable=False)
    school_id = db.Column(db.Integer, db.ForeignKey('school.id'), nullable=False)
    school = db.relationship('School', backref=db.backref('schools', lazy=True))
    created_on = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    updated_on = db.Column(db.DateTime, onupdate=datetime.datetime.utcnow())

    def __repr__(self):
        return "<Course '{} ' ".format(self.named)