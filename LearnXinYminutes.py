"""Chú thích: tất cả sẽ đc viết thành lệch,chạy trực tiếp khi compile bằng python(vì vừa dịch vừa học ^^).
    Mình sẽ dùng bản Python 3.
    Được dịch từ trang LearnXinYminutes.com
"""
# Dùng kí tự (#) để tạo comment

""" Dùng 3 dấu ngoặc kép (") để
    đánh trên nhiều dòng.
    Hoặc, có thể sử dụng để comment
"""

############################################################
# 1.Khởi đầu và tính toán trong Python
############################################################

# Số
print(3)  # in ra số 3

# 4 phép tính cơ bản
print(1 + 1)  # 2
print(8 - 1)  # 7
print(10 * 2)  # 20
print(35 / 5)  # 7.0

# Kết quả của phép chia số nguyên thì sẽ bị lược mất phần số thập phân
print(5 // 3)  # 1
print(5.0 // 3.0)  # 1.0
print(-5 // 3)  # -2
print(-5.0 // 3.0)  # -2.0

# Phép chia bình thường thì sẽ hiển thị phần thập phân
print(10.0 / 3)  # 3.3333333335
print(10 / 3)  # 3.3333333335  (cả 3 giống nhau)
print(10 / 3.0)  # 3.3333333335

# Phép chia lấy dư %
print(7 % 3)  # 1
print(5 % 3)  # 2

# Phép mũ
print(2 ** 4)  # 2^4 = 16

# Giá trị Boolean(Chú ý: chữ cái đầu viết hoa)
print(True)  # True
print(False)  # False

print(True and False)  # False # "and" và "or" là chữ nhỏ
print(True or False)  # True

# not (ý phủ định)
print(not True)  # False
print(not False)  # True

# Số nguyên trong tính toán Boolean
print(0 and 2)  # 0
print(-5 or 0)  # -5
print(0 == False)  # True
print(2 == True)  # False
print(1 == True)  # True

# So sánh bằng
print(1 == 1)  # True
print(2 == 1)  # False

# So sánh không bằng
print(1 != 1)  # False
print(1 != 2)  # True

# So sánh lớn hơn, nhỏ hơn
print(1 < 10)  # True
print(1 > 10)  # False

# So sánh lơn hơn hoặc bằng,nhỏ hơn hoặc bằng
print(1 <= 2)  # True
print(1 >= 2)  # False
print(1 >= 1)  # True

# So sánh liên tiếp
print(1 < 2 < 3)  # True
print(2 < 3 < 2)  # False

# 'is' và '=='
# 'is' thì 2 biến số cùng trỏ đến một đối tượng(Object)
# Ngược lại '==' thì 2 biến số trỏ đến 2 đối tượng khác nhau
a = [1, 2, 3, 4]  # Khai báo biến mảng a
b = a  # Khai baos biến b trỏ đến a
print(b is a)  # True vì cùng a và b cùng trỏ đến cùng 1 object
print(b == a)  # True vì như trên nên giá trị bằng nhau

b = [1, 2, 3, 4]  # Khai báo biến mảng mới b
print(b is a)  # False vì a và b trỏ đến 2 object khác nhau
print(b == a)  # True vì giá trị giống nhau

# Sử dụng dấu ngoặc kép " hoặc ngoặc đơn ' để tạo chuỗi
print("This is String")  # This is String
print('This is also a String')  # This is also a String

# Cộng chuỗi (không nên sử dụng)
a = "hello "
b = 'world'
print(a + b)  # hello world

# Thêm trực tiếp (không cần dùng dấu '+')
print('hello ''world')      # hello world
print("This is a string"[0])
print("This is a string"[1])
print("This is a string"[2])
print("This is a string"[3])

# Độ dài chuỗi len()
print(len("Hello World"))       # 11




