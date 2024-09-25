from pymongo import MongoClient

# Kết nối đến MongoDB (thay đổi URL nếu cần)
client = MongoClient('mongodb://localhost:27017/')

# Lựa chọn database (thay 'my_database' bằng tên database của bạn)
db = client['BT_tuan2']


# Thêm dữ liệu vào collection (thay thế cursor.execute bằng cách sử dụng collection.insert_one)
# def insert_data(data):
#     collection.insert_one(data)
#     print("Data inserted into MongoDB successfully.")

# # Ví dụ thêm một user mới vào MongoDB
# insert_data({
#     "username": "john_doe",
#     "email": "john@example.com"
# })
