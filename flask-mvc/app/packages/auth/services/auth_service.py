from app.repositories.user_repository import find_by_email
from werkzeug.security import check_password_hash
import jwt
import os
from datetime import datetime, timedelta

def authenticate_user(email, password):
    # Kiểm tra xem email có tồn tại không
    user = find_by_email(email)
    if not user:
        raise Exception('Email không tồn tại')

    # Kiểm tra mật khẩu
    if not check_password_hash(user['password'], password):
        raise Exception('Mật khẩu không đúng')

    # Tạo JWT token
    token = jwt.encode({
        'id': user['id'],
        'email': user['email'],
        'exp': datetime.utcnow() + timedelta(hours=1)
    }, os.getenv('JWT_SECRET_KEY'), algorithm="HS256")

    return user, token
