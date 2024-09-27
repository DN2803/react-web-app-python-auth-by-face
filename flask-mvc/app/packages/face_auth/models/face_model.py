from flask_pymongo import PyMongo
from pymongo import MongoClient
import numpy as np 
class FaceModel:
    def __init__(self, mongo):
        self.mongo = mongo
        self.collection = self.mongo.users

    def create_face_user(self, email, save_data):
        user = self.collection.find_one({"email": email})
        print (user)
        if user:
            # Update the user document to add the face_feature field
            update_result = self.collection.update_one(
                {"email": email},
                {"$set": {"face_feature": save_data}}  # Assuming data contains face_feature
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
    def remove_face_feature(self,email):
        result = self.collection.find_one_and_update(
            {"email": email},
            {"$unset": {"face_feature": 1}},  # Unset the Face_feature field
            return_document=True
        )
        print (result)
        return result
    def have_face_feature(self, email):
        document = self.collection.find_one({ "email": email, "face_feature": { "$exists": True } })
        if document:
            print("Người dùng với email '{}' có trường 'face_feature'.".format(email))
            return True 
        else:
            print("Không tìm thấy người dùng với email '{}' có trường 'face_feature'.".format(email))
            return False