from pymongo import MongoClient

# Kết nối đến MongoDB (thay đổi URL nếu cần)
client = MongoClient('mongodb://localhost:27017/')

# Lựa chọn database (thay 'my_database' bằng tên database của bạn)
db = client['demo-app-react-face-auth']


