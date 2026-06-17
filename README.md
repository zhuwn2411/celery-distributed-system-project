# Hệ thống xử lý tác vụ phân tán sử dụng Celery

## Giới thiệu

Đây là dự án minh họa cơ chế xử lý tác vụ bất đồng bộ và phân tán bằng **Celery** kết hợp với **Redis** trong Python. Hệ thống cho phép các tác vụ được đưa vào hàng đợi và xử lý bởi các Worker chạy nền thay vì thực hiện trực tiếp trên ứng dụng chính.

Dự án được thực hiện trong khuôn khổ môn học **Ứng dụng phân tán** nhằm tìm hiểu nguyên lý hoạt động của Celery và mô hình Distributed Task Queue.

---

## Công nghệ sử dụng

* Python 3.13
* Celery 5.x
* Redis / Memurai
* Flask
* Git & GitHub

---

## Cấu trúc dự án

```text
celery-distributed-system-project/
│
├── app.py
├── tasks.py
├── test.py
├── load_test.py
├── requirements.txt
└── README.md
```

### Mô tả

* **app.py**: Ứng dụng Flask và các API xử lý yêu cầu.
* **tasks.py**: Định nghĩa Celery Task và cấu hình Redis.
* **test.py**: Gửi thử một tác vụ đơn lẻ.
* **load_test.py**: Gửi nhiều tác vụ để kiểm tra khả năng xử lý tải.
* **requirements.txt**: Danh sách thư viện cần cài đặt.

---

## Chức năng của hệ thống

### Chức năng chính

* Xử lý tác vụ phân tán bằng Celery và Redis.

### Tính năng mở rộng 1

**Task Status Monitoring**

* Theo dõi trạng thái xử lý của tác vụ thông qua Task ID.
* Hỗ trợ các trạng thái:

  * PENDING
  * STARTED
  * SUCCESS
  * FAILURE

### Tính năng mở rộng 2

**Multi-Worker Load Balancing**

* Hỗ trợ nhiều Celery Worker cùng xử lý tác vụ.
* Redis tự động phân phối các Task cho các Worker đang sẵn sàng.
* Tăng khả năng xử lý song song và mở rộng hệ thống.

---

## Hướng dẫn cài đặt

### Bước 1: Tạo môi trường ảo

```bash
python -m venv venv
```

### Bước 2: Kích hoạt môi trường ảo

```bash
venv\Scripts\activate
```

### Bước 3: Cài đặt thư viện

```bash
pip install -r requirements.txt
```

---

## Khởi động Redis

Đảm bảo Redis hoặc Memurai đang hoạt động.

Kiểm tra kết nối:

```bash
memurai-cli ping
```

Kết quả:

```text
PONG
```

---

## Khởi động Celery Worker

```bash
python -m celery -A tasks worker --pool=solo --loglevel=info
```

Nếu thành công sẽ xuất hiện:

```text
Connected to redis://localhost:6379/0
celery@LAPTOP-xxxx ready
```

---

## Khởi động ứng dụng Flask

```bash
python app.py
```

Truy cập:

```text
http://127.0.0.1:5000
```

---

## Các API của hệ thống

### Tạo tác vụ mới

```text
/add/<x>/<y>
```

Ví dụ:

```text
/add/5/10
```

Kết quả:

```json
{
  "task_id": "xxxx",
  "status": "PENDING"
}
```

---

### Kiểm tra trạng thái tác vụ

```text
/status/<task_id>
```

Ví dụ:

```json
{
  "task_id": "xxxx",
  "status": "SUCCESS",
  "result": {
    "result": 15,
    "task_id": "xxxx",
    "processing_time": 4
  }
}
```

---

## Kiểm thử tải

Gửi đồng thời nhiều tác vụ:

```bash
python load_test.py
```

Kết quả:

```text
Submitted 50 tasks
```

Các Worker sẽ nhận và xử lý các tác vụ từ hàng đợi Redis.

---

## Kết luận

Dự án đã xây dựng thành công hệ thống xử lý tác vụ phân tán sử dụng Celery và Redis. Hệ thống hỗ trợ xử lý bất đồng bộ, theo dõi trạng thái tác vụ và cân bằng tải giữa nhiều Worker, góp phần minh họa rõ cơ chế hoạt động của mô hình Distributed Task Queue.
