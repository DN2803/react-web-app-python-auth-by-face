from pymongo.errors import DuplicateKeyError
class UserModel:
    def __init__(self, mongo):
        self.mongo = mongo
        self.collection = self.mongo.users

    def create_user(self, data):
        try:
            if self.collection.find_one({"email": data['email']}):
                return {"error": "User already exists"}, 400
            result = self.collection.insert_one(data)
            return {"_id": str(result.inserted_id)}, 201
        except DuplicateKeyError:
            return {"error": "User already exists"}, 400

    def get_user_by_email(self, email): 
        user = self.collection.find_one({"email": email})
        if user:
            user["_id"] = str(user["_id"])  # Chuyển ObjectId sang chuỗi
            return user
        return None


