from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance

import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

from app.packages.face_auth.models.face_model import FaceModel
from app.config.Database import db

import jwt
import os
from datetime import datetime, timedelta

def draw_landmarks_on_image(rgb_image, detection_result):
  face_landmarks_list = detection_result.face_landmarks
  annotated_image = np.copy(rgb_image)

  # Loop through the detected faces to visualize.
  for idx in range(len(face_landmarks_list)):
    face_landmarks = face_landmarks_list[idx]

    # Draw the face landmarks.
    face_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
    face_landmarks_proto.landmark.extend([
      landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y, z=landmark.z) for landmark in face_landmarks
    ])

    solutions.drawing_utils.draw_landmarks(
        image=annotated_image,
        landmark_list=face_landmarks_proto,
        connections=mp.solutions.face_mesh.FACEMESH_TESSELATION,
        landmark_drawing_spec=None,
        connection_drawing_spec=mp.solutions.drawing_styles
        .get_default_face_mesh_tesselation_style())
    solutions.drawing_utils.draw_landmarks(
        image=annotated_image,
        landmark_list=face_landmarks_proto,
        connections=mp.solutions.face_mesh.FACEMESH_CONTOURS,
        landmark_drawing_spec=None,
        connection_drawing_spec=mp.solutions.drawing_styles
        .get_default_face_mesh_contours_style())
    solutions.drawing_utils.draw_landmarks(
        image=annotated_image,
        landmark_list=face_landmarks_proto,
        connections=mp.solutions.face_mesh.FACEMESH_IRISES,
          landmark_drawing_spec=None,
          connection_drawing_spec=mp.solutions.drawing_styles
          .get_default_face_mesh_iris_connections_style())

  return annotated_image

def plot_face_blendshapes_bar_graph(face_blendshapes):
  # Extract the face blendshapes category names and scores.
  face_blendshapes_names = [face_blendshapes_category.category_name for face_blendshapes_category in face_blendshapes]
  face_blendshapes_scores = [face_blendshapes_category.score for face_blendshapes_category in face_blendshapes]
  # The blendshapes are ordered in decreasing score value.
  face_blendshapes_ranks = range(len(face_blendshapes_names))

  fig, ax = plt.subplots(figsize=(12, 12))
  bar = ax.barh(face_blendshapes_ranks, face_blendshapes_scores, label=[str(x) for x in face_blendshapes_ranks])
  ax.set_yticks(face_blendshapes_ranks, face_blendshapes_names)
  ax.invert_yaxis()

  # Label each bar with values
  for score, patch in zip(face_blendshapes_scores, bar.patches):
    plt.text(patch.get_x() + patch.get_width(), patch.get_y(), f"{score:.4f}", va="top")

  ax.set_xlabel('Score')
  ax.set_title("Face Blendshapes")
  plt.tight_layout()
  plt.show()


base_options = python.BaseOptions(model_asset_path='face_landmarker_v2_with_blendshapes.task')
options = vision.FaceLandmarkerOptions(base_options=base_options,
                                       output_face_blendshapes=True,
                                       output_facial_transformation_matrixes=True,
                                       num_faces=1)
detector = vision.FaceLandmarker.create_from_options(options)

def compare_landmarks(landmarks1, landmarks2, threshold=0.5):
    distances = []
    for p1, p2 in zip(landmarks1, landmarks2):
        dist = distance.euclidean(p1, p2)
        distances.append(dist)

    mean_distance = np.mean(distances)
    # Kiểm tra xem khoảng cách trung bình có nhỏ hơn ngưỡng không
    return mean_distance < threshold

def create_new_face_auth(email, data):
    detection_result = detector.detect(data)
    save_data = detection_result.facial_transformation_matrixes
    face_model = FaceModel(db)
    face_model.create_face_user(email, save_data)
def authenticate_user_by_face(data): 
    face_model = FaceModel(db)

    users = face_model.get_all_users_with_face_feature()
    # Kiểm tra nếu không có người dùng
    if not users:
        return None, None
    input_face_feature = detector.detect(data).facial_transformation_matrixes
    # Duyệt qua tất cả người dùng và so sánh face_feature
    for user in users:
        # Giả sử có hàm compare_face_features để so sánh hai đặc điểm khuôn mặt
        if compare_landmarks(input_face_feature, user['face_feature']):
            # Tạo JWT token nếu tìm thấy người dùng
            token = jwt.encode({
                'email': user['email'],
                'exp': datetime.utcnow() + timedelta(hours=1)  # Thời gian hết hạn là 1 giờ
            }, os.getenv('JWT_SECRET_KEY'), algorithm="HS256")
            return user, token

    # Nếu không tìm thấy người dùng nào phù hợp
    return None, None
    return user, token