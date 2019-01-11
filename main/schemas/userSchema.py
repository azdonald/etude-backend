from marshmallow import Schema, fields, post_load
from main.models.userModels import User, TutorProfile


class UserSchema(Schema):
    firstname = fields.Str()
    lastname = fields.Str()
    email = fields.Str()
    publicId = fields.Str()
    password = fields.Str()
    created_on = fields.DateTime()
    user_type  = fields.Int()

    @post_load
    def make_user(self, data):
        return User(**data)


class TutorProfileSchema(Schema):
    bio = fields.Str()
    rate = fields.Str()

    @post_load
    def make_profile(self, data):
        return TutorProfile(**data)