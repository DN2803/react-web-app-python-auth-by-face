from flask import Flask, request, jsonify
from app.packages.auth.services.auth_service import authenticate_user
from app.packages.auth.services.auth_service import create_new_user
from app import app

@app.route('/api/login', methods=['POST'])
def login():
    
    # Nhận thông tin đăng nhập từ request
    email = request.json.get('email')
    password = request.json.get('password')
    if not email or not password:
        return jsonify({"error": "Missing email or password"}), 400
    
    # Gọi auth service để xác thực
    token = authenticate_user(email, password)
    
    if token:
        return jsonify({"message": "Login successful", "token": token}), 200
    else:
        return jsonify({"error": "Authentication failed"}), 401


@app.route('/api/register', methods=['POST'])  
def register():
    data = request.json
    if not data or 'email' not in data or 'password' not in data:  # Validate data
        return jsonify({"error": "Missing required fields"}), 400

    result = create_new_user(data)
    
    # Check if result indicates an error (assuming create_new_user returns a tuple with status)
    if isinstance(result, tuple):
        return jsonify(result[0]), result[1]
    
    return jsonify({"message": "User created successfully"}), 201  # Response for successful registration

