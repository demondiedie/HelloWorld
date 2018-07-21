"""6. MODULE"""
# Hướng đối tượng
#Python có một cách đặt các định nghĩa vào một tập tin và dùng chúng trong một kịch bản
#   hoặc trong một phiên làm việc với trình thông dịch. Tập tin này được gọi là Module
"""Module là một tập tin chứa các định nghĩa và câu lệnh Python.Tên của tập tin là tên của module
    với đuôi .py được gắn vào.Trong một module, tên của module(là một chuỗi)
"""
#Ví dụ: tạo một tâp tin tên fibo.py với nội dung:
"""
# Fibonacci numbers module
def fib(n): #write fibonacci series up to n
    a,b = 0,1
    while b<n:
        print(b)
        a,b=b,a+b
def fib2(n): #return fibonacci series up to n
    result = []
    a,b = 0,1
    while b<n:
        result.append(b)
        a,b=b,a+b
    return result
"""
import fibo #Nhập module
fibo.fib(200)
fi = fibo.fib # Có thể gán vào một tên cục bộ
fi(500)
print(list(fibo.fib2(100)))

###6.1 Bàn thêm về module
# Module có thể nhập các module khác.Thông thường ta hay để tất cả các lệnh import ở đầu một module
# Cách khác: có thể lấy tùy chọn method từ một module.
print("-"*50)
from fibo import fib,fib2
fib(50)

#hoặc nhập tất cả method trừ method bắt đầu bằng dấu gạch chân (_)
from fibo import *
fib(10)

###6.1.1 Đường dẫn tìm module
# Khi module ten fibo được nhập vào, trình thông dịch sẽ tìm một tập tin tên fibo.py trong thư mục hiện tại,
#   rồi trong danh sách các thư mục được chỉ định bởi biến môi trường PYTHONPATH. Biến này có cùng cú pháp
#   như là biến môi trường PATH,cùng chứa một danh sách tên các thư mục.
#   Khi PYTHONPATH chưa được thiết lập,hoặc khi tập tin không được tìm thấy,thì sẽ tìm trong thư mục cài python

###6.1.2 Các tập tin Python đã dịch

###6.2 Các module chuẩn
#Python có một thư viện các module chuẩn. Một vài module được chuyển thẳng vào trình thông dịch
#Ví dụ module sys:
"""import sys
sys.path.append("/ufs/guido/lib/python")
"""
# Biến sys.path là một danh sách các chuỗi quyết định đường dẫn tìm kiếm các module của trình thông dịch.

###6.3 dir() hàm
# Hàm có sẵn dir() được dùng để tìm các method trong  một module định nghĩa
# dir() liệt kê mọi loại tên: biến,module,hàm,...
print(dir(fibo))
import sys
print(dir(sys))

###6.4 Gói (Package)

###6.4.1 Nhập * từ một Package

###6.4.2 Tham chiếu nội trong gói

###6.4.3 Package trong nhiều thư mục

