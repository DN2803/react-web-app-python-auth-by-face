from flask import request, jsonify
from .auth_controller import AuthController
from ..services.password_service import PasswordService
class PasswordController(AuthController):
    def __init__(self, service = PasswordService()):
        super().__init__(service)

    def resetPassword(self, data):
        is_done = self.service.resetPassword(data)
        if is_done:  
            return jsonify({"message": "Reseted password"}), 200
        else:
            return jsonify({"error": "User not found"}), 404
        
    
password_controller = PasswordController()