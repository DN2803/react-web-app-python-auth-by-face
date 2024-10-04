import numpy as np 
from app.config.Database import db

from .auth_model import AuthModel

class FaceModel(AuthModel): 
    def __init__(self, mongo=db):
        super().__init__(mongo=mongo)
    def get_authen_method(self, email):
        user = super().get_by_email(email)
        if user and "face_feature" in user: 
            return user["face_feature"]
        else:
            return None

    # def create_face_user(self, email, save_data):
    #     user = self.collection.find_one({"email": email})
    #     if user:
    #         # Update the user document to add the face_feature field
    #         update_result = self.collection.update_one(
    #             {"email": email},
    #             {"$set": {"face_feature": save_data}}  # Assuming data contains face_feature
    #         )
    #         # Check if the update was successful
    #         if update_result.modified_count > 0:
    #             return {"message": "Face feature added successfully"}, 201
    #         else:
    #             return {"message": "No changes made to the user"}, 400
    #     else:
    #         return {"error": "User not found"}, 404


    # def remove_face_feature(self,email):
    #     result = self.collection.find_one_and_update(
    #         {"email": email},
    #         {"$unset": {"face_feature": 1}},  # Unset the Face_feature field
    #         return_document=True
    #     )
    #     print (result)
    #     return result
    # def have_face_feature(self, email):
    #     document = self.collection.find_one({ "email": email, "face_feature": { "$exists": True } })
    #     if document:
    #         print("Người dùng với email '{}' có trường 'face_feature'.".format(email))
    #         return True 
    #     else:
    #         print("Không tìm thấy người dùng với email '{}' có trường 'face_feature'.".format(email))
    #         return False