from flask_jwt_extended import create_access_token, get_jwt_claims
from . import jwt


@jwt.user_claims_loader
def addDetailsToToken(user):
    return {'id': user['id'], 'pid': user['publicid'], 
            'type': user['user_type'], 'name': user['firstname']}

def generateToken(user):
    return create_access_token(user)

def getUserDetails():
    return get_jwt_claims()