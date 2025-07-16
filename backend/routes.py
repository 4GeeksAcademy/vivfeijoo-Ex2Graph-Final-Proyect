from flask import Blueprint, request, jsonify
from backend.models import db, User
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

api = Blueprint("api", __name__)

from flask import Blueprint

api = Blueprint('api', __name__)

@api.route('/')
def home():
    return {"message": "✅ API is working!"}

@api.route("/register", methods=["POST"])
def register():
    data = request.json
    user = User(email=data["email"])
    user.set_password(data["password"])
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201

@api.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(email=data["email"]).first()
    if user and user.check_password(data["password"]):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token)
    return jsonify({"message": "Invalid credentials"}), 401

@api.route("/private", methods=["GET"])
@jwt_required()
def private():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    return jsonify(message=f"Welcome {user.email} to your private route!")
