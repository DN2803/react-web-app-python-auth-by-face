from flask import request, jsonify
import base64
import cv2
import numpy as np

from auth_controller import AuthController
from ..services.face_service import FaceService
from app import app


class FaceController(AuthController):
    def __init__(self, service=FaceService):
        super().__init__(service)

    def __json2image (self, image_data):
        if not image_data:  # Validate data
            return None
                # Tách phần prefix "data:image/jpeg;base64," (nếu có) để lấy dữ liệu base64
        header, encoded = image_data.split(',', 1)
        image_bytes = base64.b64decode(encoded)  # Giải mã dữ liệu base64
        # Chuyển đổi byte stream thành numpy array
        image_array = np.frombuffer(image_bytes, dtype=np.uint8)
        # Giải mã dữ liệu hình ảnh từ numpy array
        image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
        return image

    def login(self, data): 
        image_data = self.__json2image(data["image"])
        data["image"] = image_data
        return super().login(data)
    

# @app.route('/api/create_face_auth', methods=['POST'])
# def create_new_auth_method():
#     data = request.json
#     image_data = data.get('image')
#     email = data.get('email')
#     if not data or not image_data or not email:  # Validate data
#         return jsonify({"error": "Missing required fields"}), 400
#             # Tách phần prefix "data:image/jpeg;base64," (nếu có) để lấy dữ liệu base64
#     header, encoded = image_data.split(',', 1)
#     image_bytes = base64.b64decode(encoded)  # Giải mã dữ liệu base64
#     # Chuyển đổi byte stream thành numpy array
#     image_array = np.frombuffer(image_bytes, dtype=np.uint8)

#     # Giải mã dữ liệu hình ảnh từ numpy array
#     image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

#     result = face_service.create_new_face_auth(email, image)
    
#     # Check if result indicates an error (assuming create_new_user returns a tuple with status)
#     if isinstance(result, tuple):
#         return jsonify(result[0]), result[1]
    
#     return jsonify({"message": "Face authentication created successfully"}), 201  # Response for successful registration



# @app.route('/api/remove_face_auth', methods=['POST'])
# def remove_face_auth():
#     email = request.json.get('email')
#     print(f"Received email: {email}")
        
#     model = face_model.FaceModel(face_service.db)
#     updated_user = model.remove_face_feature(email)
        
#     if updated_user:  
#         return jsonify({"message": "FaceID status deleted successfully"}), 200
#     else:
#         return jsonify({"error": "User not found"}), 404
# @app.route('/api/check_face_auth', methods= ['POST'])
# def check_face_auth():
#     email  = request.json.get('email')
#     model = face_model.FaceModel(face_service.db)
#     is_not_empty = model.have_face_feature(email)
#     if is_not_empty:  
#         return jsonify({"message": "FaceID status True", "user": is_not_empty}), 200
#     else:
#         return jsonify({"error": "User not found"}), 404