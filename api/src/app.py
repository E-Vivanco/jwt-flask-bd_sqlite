import os
import datetime
from flask import Flask, jsonify, request
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager,get_jwt_identity,create_access_token,jwt_required
from werkzeug.security import generate_password_hash,check_password_hash
from config import DevelopmentConfig
from routes  import login,profile,users
from models import db,  User, Profile


app = Flask(__name__)
app.config.from_object(DevelopmentConfig())

db.init_app(app)
Migrate(app, db)
CORS(app)
jwt = JWTManager(app)

app.register_blueprint(users.bpUsers, url_prefix='/api')
app.register_blueprint(login.bpLogin, url_prefix='/api')
app.register_blueprint(profile.bpProfile, url_prefix='/api')


@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def main():
    return jsonify({ "message": "Welcome to my API REST Flask" }), 200


with app.app_context():
    db.create_all()

if __name__ == '__main__':
   app.run()