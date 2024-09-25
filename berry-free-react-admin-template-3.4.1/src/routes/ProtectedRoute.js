import React from 'react';
import { Navigate } from 'react-router-dom';
import { useAuth } from 'path_to_your_auth_context'; // Đường dẫn tới AuthContext

const ProtectedRoute = ({ children }) => {
  const { token } = useAuth(); // Lấy token từ AuthContext

  if (!token) {
    // Nếu không có token, chuyển hướng đến trang đăng nhập
    return <Navigate to="/pages/login/login3" replace />;
  }

  return children; // Nếu có token, hiển thị các component con
};

export default ProtectedRoute;
