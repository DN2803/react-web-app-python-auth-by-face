import torch
from PIL import Image
from facenet_pytorch import InceptionResnetV1, MTCNN
import numpy as np
from numpy.linalg import norm

# Khởi tạo model FaceNet
model = InceptionResnetV1(pretrained='vggface2').eval()

# Sử dụng MTCNN để phát hiện và cắt khuôn mặt
mtcnn = MTCNN(keep_all=False, device='cpu')  # Giữ lại chỉ một khuôn mặt

from app.packages.face_auth.models.face_model import FaceModel
from app.config.Database import db

import jwt
import os
from datetime import datetime, timedelta



def compare(embedding1, embedding2, threshold=0.6):
    # Chuẩn hóa L2 các vector đặc trưng
    embedding1_norm = embedding1 / norm(embedding1)
    embedding2_norm = embedding2 / norm(embedding2)

    # Tính khoảng cách Euclid
    euclidean_distance = np.linalg.norm(embedding1_norm - embedding2_norm)
    # Quyết định nếu hai khuôn mặt có thể là cùng một người
    if euclidean_distance < threshold:
        return True
    else:
        return False

def create_new_face_auth(email, image):
    face = mtcnn(image)

    if face is not None:
        # Chuyển đổi khuôn mặt thành vector đặc trưng
        face_embedding = model(face.unsqueeze(0))  # Thêm chiều batch
        feature = face_embedding.squeeze(0).detach().numpy().tolist()

        save_data = feature
        face_model = FaceModel(db)
        face_model.create_face_user(email, save_data)
def authenticate_user_by_face(image): 
    face_model = FaceModel(db)

    users = face_model.get_all_users_with_face_feature()
    # Kiểm tra nếu không có người dùng
    if not users:
        return None, None
    face = mtcnn(image)

    if face is None:
        return None, None
    # Chuyển đổi khuôn mặt thành vector đặc trưng
    face_embedding = model(face.unsqueeze(0))  # Thêm chiều batch
    input_face_feature = face_embedding.squeeze(0).detach().numpy()
    # Duyệt qua tất cả người dùng và so sánh face_feature
    for user in users:
        # Giả sử có hàm compare_face_features để so sánh hai đặc điểm khuôn mặt
        if compare(input_face_feature, np.array(user['face_feature'])):
            # Tạo JWT token nếu tìm thấy người dùng
            token = jwt.encode({
                'email': user['email'],
                'exp': datetime.utcnow() + timedelta(hours=1)  # Thời gian hết hạn là 1 giờ
            }, os.getenv('JWT_SECRET_KEY'), algorithm="HS256")
            return user, token

    # Nếu không tìm thấy người dùng nào phù hợp
    return None, None
