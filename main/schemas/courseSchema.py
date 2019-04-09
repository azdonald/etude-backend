from marshmallow import Schema, fields, post_load
from main.models.schoolModels import Course


class UserSchema(Schema):
    course_name = fields.Str()
    publicId = fields.Str()
    created_on = fields.DateTime()

    @post_load
    def make_user(self, data):
        return Course(**data)
