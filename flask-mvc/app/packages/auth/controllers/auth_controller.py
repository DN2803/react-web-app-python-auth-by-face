from flask import Flask, request, jsonify
from app.packages.auth.services.auth_service import authenticate_user

from app import app

@app.route('/api/login', methods=['POST'])
def login():
    
    # Nhận thông tin đăng nhập từ request
    email = request.json.get('email')
    password = request.json.get('password')
    print("hello ", email, password)
    if not email or not password:
        return jsonify({"error": "Missing email or password"}), 400
    
    # Gọi auth service để xác thực
    token = 0#authenticate_user(email, password)
    
    if token:
        return jsonify({"message": "Login successful", "token": token}), 200
    else:
        return jsonify({"error": "Authentication failed"}), 401


