from flask_pymongo import PyMongo
from pymongo import MongoClient
class FaceModel:
    def __init__(self, mongo):
        self.mongo = mongo
        self.collection = self.mongo.users

    def create_face_user(self, email, data):
        user = self.collection.find_one({"email": email})
        if user:
            # Update the user document to add the face_feature field
            update_result = self.collection.update_one(
                {"email": email},
                {"$set": {"face_feature": data["face_feature"]}}  # Assuming data contains face_feature
            )
        
            # Check if the update was successful
            if update_result.modified_count > 0:
                return {"message": "Face feature added successfully"}, 201
            else:
                return {"message": "No changes made to the user"}, 400
        else:
            return {"error": "User not found"}, 404
    def get_all_users_with_face_feature(self):
        # Tìm tất cả người dùng có face_feature
        users = self.collection.find({"face_feature": {"$exists": True}})  
        
        # Chuyển đổi kết quả từ cursor sang danh sách và chuyển ObjectId sang chuỗi
        user_list = []
        for user in users:
            user["_id"] = str(user["_id"])  # Chuyển ObjectId sang chuỗi
            user_list.append(user)

        # Trả về danh sách người dùng hoặc None nếu không tìm thấy
        return user_list if user_list else None
