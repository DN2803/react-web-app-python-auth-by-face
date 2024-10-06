from .auth_controller import AuthController
from ..services.password_service import PasswordService
class PasswordController(AuthController):
    def __init__(self, service = PasswordService()):
        super().__init__(service)
    
password_controller = PasswordController()