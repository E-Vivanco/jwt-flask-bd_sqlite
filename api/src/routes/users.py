from models import User, Profile
from flask import Blueprint, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required
from werkzeug.security import generate_password_hash, check_password_hash

bpUsers = Blueprint('bpUsers', __name__)

@bpUsers.route('/users', methods=['GET'])
def all_users():

    users = User.query.all()  # [<User 1>, <User 2>]
    users = list(map(lambda user: user.serialize_profile(), users))

    return jsonify(users), 200
