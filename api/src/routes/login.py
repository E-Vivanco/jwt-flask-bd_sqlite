from models import User, Profile
import datetime
from flask import Blueprint, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required
from werkzeug.security import generate_password_hash, check_password_hash


bpLogin = Blueprint('bpLogin', __name__)

@bpLogin.route('/login', methods=['POST'])
def login():
    try:
            email = request.json.get('email')
            password = request.json.get('password')

            if not email: return jsonify({"message": "Email is required"}), 400
            if not password: return jsonify({"message": "Password is required"}), 400

            foundUser = User.query.filter_by(email=email).first()

            if not foundUser: return jsonify({"message": "Email/Password are incorrects"}), 401
            if not check_password_hash(foundUser.password, password): return jsonify({"message": "Email/Password are incorrects"}), 401


            expires = datetime.timedelta(days=30)
            access_token = create_access_token(identity=foundUser.id, expires_delta=expires)

            data = {
                "access_token": access_token,
                "user": foundUser.serialize()
            }

            return jsonify(data), 200
    except Exception as e:
            print(e)
            return jsonify({"msg":"intenta mas tarde"}), 200

@bpLogin.route('/register', methods=['POST'])
def register():
    try:
        email = request.json.get('email')
        password = request.json.get('password')
        biography = request.json.get('biography', "")
        linkedin = request.json.get('linkedin', "")
        github = request.json.get('github', "")
        facebook = request.json.get('facebook', "")

        if not email: return jsonify({"message": "Email is required"}), 400
        if not password: return jsonify({"message": "Password is required"}), 400

        foundUser = User.query.filter_by(email=email).first()
        if foundUser: return jsonify({"message": "Email already exists"}), 400

        user = User()

        user.email = email
        user.password = generate_password_hash(password)

        profile = Profile()
        profile.biography = biography
        profile.linkedin = linkedin
        profile.github = github
        profile.facebook = facebook

        user.profile = profile
        user.save()

        if user:
            expires = datetime.timedelta(days=30)
            access_token = create_access_token(identity=user.id, expires_delta=expires)

            data = {
                "access_token": access_token,
                "user": user.serialize()
            }

            return jsonify(data), 201
    except Exception as e:
            print(e)

            return jsonify({ "message": "Please try again later."}), 400
