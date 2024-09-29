# Hệ thống xác thực dựa vào mặt người

## 1. Giới thiệu

Dự án này là hệ thống xác thực dựa vào mặt người được xây dựng trên nền tảng web. Dự án này bao gồm giao diện người dùng (front-end) và phần quản lý dữ liệu (back-end) được xây dựng bằng React.js và Python (Flask)

Ứng dụng này cung cấp các tính năng đăng nhập bằng khuôn mặt và mật khẩu truyền thống và quản lý dữ liệu thông qua API REST, với giao diện người dùng thân thiện và hiệu quả.

## 2. Tính năng

- **Người dùng**: Đăng ký, đăng nhập, xác thực.
- **Quản lý tài khoản**: Bật tắt xác thực khuôn mặt.
- **Tương tác dữ liệu**: Tạo, đọc, cập nhật, xóa (CRUD) dữ liệu từ backend thông qua API REST.
- **Giao diện**: Giao diện front-end hiện đại, thân thiện với người dùng.
- **Bảo mật**: Sử dụng xác thực JWT (JSON Web Tokens) cho bảo mật.

## 3. Cấu trúc thư mục

Dự án này bao gồm hai phần chính: Front-end và Back-end.

```bash
project-name/
├── backend/                 # Backend (Python)
│   ├── controllers/         # Các controller xử lý logic API
│   ├── models/              # Các model của cơ sở dữ liệu (MongoDB)
│   ├── routes/              # Định tuyến API
│   ├── config/              # Cấu hình kết nối DB, bảo mật JWT, v.v.
│   └── server.py            # Điểm khởi động của backend
│
├── frontend/                # Frontend (React.js)
│   ├── src/                 # Code chính của ứng dụng React
│   ├── components/          # Các component UI
│   ├── pages/               # Các trang của ứng dụng (Home, Login, Dashboard)
│   └── App.js               # Entry point chính của frontend
│
└── README.md                # File README (hướng dẫn dự án)
```
## 4. Cài đặt

### 4.1 Yêu cầu hệ thống
- **Python** >= 3.11.0
- **npm** >= 9.6.7
- **MongoDB** 

### 4.2 Cài đặt Frontend
1. Điều hướng vào thư mục `berry-free-react-admin-template-3.4.1`:
   ```bash
   cd berry-free-react-admin-template-3.4.1
   ```
2. Cài đặt các phụ thuộc 
   ```bash
   npm install
   ```
3. Chạy ứng dụng front-end (dev-mode): 
   ```bash
   npm start
   ```
### 4.3 Cài đặt Backend
1. Điều hướng vào thư mục `flask-mvc`:
   ```bash
   cd flask-mvc
   ```
2. Cài đặt các phụ thuộc 
   ```bash
   pip install -r requirements.txt
   ```
3. Chạy ứng dụng back-end (dev-mode): 
   ```bash
   python server.py
   ```
## 5. Hướng dẫn sử dụng
Sau khi hoàn thành các bước cài đặt, bạn có thể truy cập các phần sau:

- **Frontend**: Truy cập giao diện web tại http://localhost:3000.
- **Backend API**: Các endpoint của API REST sẽ có sẵn tại http://localhost:8080/api.