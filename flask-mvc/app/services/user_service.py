from app.models.user import UserModel
from app.config.Database import db
def create_user(data):
    user_model = UserModel(db)
    user = user_model.create_user(data)
    return user

def get_users_by_email(email):
    user_model = UserModel(db)
    user = user_model.get_user_by_email(email)
    return user
