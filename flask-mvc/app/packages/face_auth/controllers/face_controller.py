from flask import Flask, request, jsonify
from app.packages.face_auth.services import face_service

from app import app

@app.route('/api/create_face_auth', methods=['POST'])
def create_new_auth_method():
    data = request.json
    if not data:  # Validate data
        return jsonify({"error": "Missing required fields"}), 400

    result = face_service.create_new_face_auth(data)
    
    # Check if result indicates an error (assuming create_new_user returns a tuple with status)
    if isinstance(result, tuple):
        return jsonify(result[0]), result[1]
    
    return jsonify({"message": "Face authentication created successfully"}), 201  # Response for successful registration


@app.route('api/face_authentication', methods=['POST'])
def face_auth():
    data = request.json
    if not data: 
        return jsonify({"error": "Missing required fields"}), 400
    # Gọi auth service để xác thực
    token = face_service.authenticate_user_by_face(data)
    
    if token:
        return jsonify({"message": "Login successful", "token": token}), 200
    else:
        return jsonify({"error": "Authentication failed"}), 401