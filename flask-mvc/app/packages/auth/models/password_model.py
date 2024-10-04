from .auth_model import AuthModel


class PasswordModel(AuthModel):
    def __init__(self, mongo):
        super().__init__(mongo)
    
    def get_authen_method(self, email):
        print (email)
        user = super().get_by_email(email)
        print (user)
        if user: 
            return user["password"]
        else:
            return None
