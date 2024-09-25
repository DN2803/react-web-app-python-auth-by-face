from werkzeug.security import generate_password_hash
import os
class Hash:
    def __init__(self):
        pass

    def get_hash(self, password):
        """Băm mật khẩu gốc."""
        return generate_password_hash(password)

# Mật khẩu cần băm
password = 'nganguyen2k3'

# Tạo thể hiện của lớp Hash
hash_util = Hash()

# Gọi phương thức get_hash thông qua thể hiện
hashed_password = hash_util.get_hash(password)

# In ra mật khẩu đã băm
print(hashed_password)

print (os.getenv('JWT_SECRET_KEY'))