from abc import abstractmethod
from app.packages.users.models.user_model import UserModel

class AuthModel(UserModel): 
    def __init__(self, mongo):
        super().__init__(mongo=mongo)
        
    @abstractmethod
    def get_authen_method(self, email):
        pass 