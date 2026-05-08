# Hệ Thống Quản Lý Sinh Viên - Nhóm 5

Đây là một dự án thực hành Python đơn giản để quản lý danh sách sinh viên thông qua giao diện dòng lệnh (CLI). Dự án được thực hiện bởi **Nhóm 5** như một phần của bài tập thực hành GitHub.

## 🚀 Tính năng chính

- **Thêm sinh viên mới**: Nhập thông tin chi tiết như Mã số sinh viên (MSSV), Họ tên, Tuổi và điểm GPA.
- **Hiển thị danh sách**: Xem toàn bộ danh sách sinh viên hiện có trong hệ thống với định dạng bảng rõ ràng.
- **Tìm kiếm thông minh**: Tìm kiếm sinh viên nhanh chóng theo Tên hoặc MSSV (không phân biệt chữ hoa/chữ thường).
- **Kiểm tra dữ liệu**: Hỗ trợ kiểm tra đầu vào để đảm bảo tính chính xác của dữ liệu.

## 📂 Cấu trúc dự án

- [main.py](file:///d:/uit-hk6/is208/lab/lab5/group5-github-practice/main.py): Điểm khởi đầu của ứng dụng, chứa menu điều hướng và logic điều khiển chính.
- [student.py](file:///d:/uit-hk6/is208/lab/lab5/group5-github-practice/student.py): Định nghĩa lớp `Student` và các phương thức xử lý dữ liệu sinh viên.
- [utils.py](file:///d:/uit-hk6/is208/lab/lab5/group5-github-practice/utils.py): Các hàm tiện ích dùng chung cho việc nhập liệu và định dạng hiển thị.

## 🛠️ Hướng dẫn sử dụng

### Yêu cầu hệ thống
- Máy tính đã cài đặt **Python 3.x**.

### Các bước thực hiện
1. Clone repository này về máy local:
   ```bash
   git clone https://github.com/[your-username]/group5-github-practice.git
   ```
2. Di chuyển vào thư mục dự án:
   ```bash
   cd group5-github-practice
   ```
3. Chạy ứng dụng:
   ```bash
   python main.py
   ```

## 📝 Ghi chú
- Dữ liệu hiện tại được lưu trữ tạm thời trong bộ nhớ (In-memory), dữ liệu sẽ bị xóa khi ứng dụng kết thúc.
- Đây là dự án phục vụ mục đích học tập và thực hành làm việc nhóm trên GitHub.

---
© 2026 - Nhóm 5 - IS208 Lab 5
