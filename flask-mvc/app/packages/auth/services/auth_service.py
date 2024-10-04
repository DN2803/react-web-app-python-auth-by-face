from abc import abstractmethod
from app.config.Database import db


from app.services.base_service import BaseService
from ..models.auth_model import AuthModel
class AuthService(BaseService): 

    def __init__(self, model= AuthModel(db), session = None):
        super().__init__(model, session)
        print(model)
    
    @abstractmethod
    def authenticate(self, data):
        pass