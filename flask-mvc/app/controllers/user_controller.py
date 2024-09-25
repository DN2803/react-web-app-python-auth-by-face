
from flask import request, jsonify
from app.services.user_service import create_user, get_users

def add_user():
    data = request.get_json()
    user = create_user(data)
    return jsonify({'message': 'User created successfully'}), 201

def list_users():
    users = get_users()
    return jsonify(users), 200
