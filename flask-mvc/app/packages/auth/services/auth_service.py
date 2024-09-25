from app.services.user_service import *
from app.config.Hash import *
import jwt
import os
from datetime import datetime, timedelta

def authenticate_user(email, password):
    # Kiểm tra xem email có tồn tại không
    user = get_users_by_email(email)
    if not user:
        raise Exception('Email không tồn tại')

    # Kiểm tra mật khẩu
    hash_util = Hash()
    if not hash_util.checkHash(user['password'], password):
        raise Exception('Mật khẩu không đúng')

    # Tạo JWT token
    token = jwt.encode({
        'email': user['email'],
        'exp': datetime.utcnow() + timedelta(hours=1)  # Thời gian hết hạn là 1 giờ
    }, os.getenv('JWT_SECRET_KEY'), algorithm="HS256")

    return user, token

def create_new_user(data):
    hash_util = Hash()  # Tạo một đối tượng Hash

    # Băm mật khẩu nếu có trong dữ liệu
    if 'password' in data:
        data['password'] = hash_util.getHash(data['password'])  # Thay thế mật khẩu bằng mật khẩu đã băm

    response = create_user(data)  # Tạo người dùng mới
    return response
