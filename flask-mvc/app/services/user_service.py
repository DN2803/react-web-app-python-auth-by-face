from app.models.user import UserModel
from app.config.Database import db
def create_user(data):
    user_model = UserModel(db)
    user = user_model.create_user(data)
    return user

def get_users():
    user_model = UserModel(db)
    users = user_model.get_all_users()
    return list(users)
