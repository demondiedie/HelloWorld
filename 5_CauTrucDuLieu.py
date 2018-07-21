"""5. CẤU TRÚC DỮ LIỆU"""
###5.1 Bàn thêm về danh sách
# Các phương thức của đối tượng danh sách:
a = [1, 2, 3, 4, 5, 6]
a.append(77)  # Thêm một đối tượng vào cuối danh sách
a.insert(0, 23)  # Chèn một phần tử vào vị trí chỉ định (vị trí,giá trị biến)
a.remove(1)  # Xóa khỏi danh sách phần tử đầu tiên có giá trị là x,Báo lỗi nếu không có phần tử như vậy
a.pop(2)  # Xóa khỏi danh sách phần tử thứ x.Nếu để trống sẽ xóa cuối danh sách.
print(a.index(77))  # Trả về vị trí của phần tử trong ngoặc "77"
print(a.count(77))  # Trả về số lần "77" xuất hiện trong d/s
a.sort()  # Sắp xếp d/s
print(a)
a.reverse()  # Đảo ngược d/s
print(a)

###5.1.1 Dùng danh sách như ngăn xếp
# Thêm một phần tử vào cuối dùng append() và lấy ra dùng pop()

###5.1.2 Dùng danh sách như hàng đợi

###5.1.3 Công cụ lập trình hướng hàm
# 1. filter(function,sequence): trả về một dãy chứa các phần tử mà function(item) có giá trị đúng.
# Ví dụ: Tìm số nguyên tố
print("-" * 50)


def f(x):
    return x % 2 != 0 and x % 3 != 0  # filter trả về dãy giá trị khi func trả về True


print(list(filter(f, range(2, 35))))

lst = [1, 5, 3, 2, 6, 7, 3, 60, 3]
print(list(filter(f, lst)))

# 2.map(function,sequence) gọi function(item) với mỗi phần tử trong dãy và trả về một danh sách các giá trị trả về.
# Ví dụ: Tính một vài số lập phương
print("-" * 50)


def cube(x):
    return x * x * x  # map trả về dãy khi tính toán trong func


print(list(map(cube, range(1, 11))))

#      Có thể truyền vào nhiều dãy
print("-" * 50)
rag = range(8)


def add(x, y): return x + y


print(list(map(add, rag, rag)))

###5.1.4 Gộp danh sách
print("-" * 50)

vec = [2, 4, 6]
vec2 = [3, 1, 6]
print(list(3 * x for x in vec))
# print("yahoo!" if 2 > 3 else 2)
print(list([x, x ** 2] for x in vec))
print([(x, x ** 2) for x in vec])
print("yahoo" if 3 > 2 else 2)
print([x if x > y else y for x in vec for y in vec2])
print([x + y for x in vec for y in vec2])
print([vec[i] * vec2[i] for i in range(len(vec))])

# Ưu điểm: gộp danh sách uyển chuyển hơn nhiều so với map()
#         Có thể áp dụng cho các biểu thức phức tạp và các hàm lồng nhau
#         Chương trình chạy nhanh hơn với cách viết truyền thống.

###5.2 del câu lệnh
a = [-1, 1, 22, 77, 23, 676, 4]
del a[0]  # >> xóa phần tử thứ 1
del a[2:4]  # >> xóa vị trí 2 và 3
del a[:]  # > xóa trắng
del a  # > xóa dãy a

###5.3 Bộ và dãy
print("-" * 50)
# tuple
t = (12345, 5342, "hello")
print(t[0])  # > in ra 12345

u = t, (1, 2, 3, 4, 5)
print(u)

singleton = "hello",  # tuple đơn (1 giá trị), có dấu phẩy
print(singleton)

print("-" * 50)
x, y, z = t  # tháo dãy
print(x)
print(y)
print(z)
print(t)

# Việc gói nhiều giá trị luôn tạo một tuple,
#  nhưng phép tháo ra có thể được áp dụng cho mọi dãy(chuỗi,danh sách,tuple)

###5.4 Tập hợp
# Một tập hợp là một nhóm các phần tử không lặp
# Hỗ trợ các toán tử: hợp, giao, hiệu và đối xứng
print("-" * 50)
basket = ["apple", "orange", "apple", "pear", "orange", "banana"]
fruit = set(basket)
print(fruit)

a = set("abracadabra")
b = set("alacazam")
print(a - b)  # hiệu
print(a | b)  # hợp
print(a & b)  # giao
print(a ^ b)  # đối xứng
print("-" * 50)
###5.5 Tu dien
# Tu dien duoc chia chi muc tu cac khoa’
# tuple co the duoc dung lam khoa neu no chi chua chuoi,so’,hoac tuple
# danh sach khong the dung lam khoa
# Tu dien la mot tap hop khong thu tu cua cac bo khoa’ gia tri., voi dieu kien khoa phair la duy nhat(trong cung mot tu dien)
tel1 = {}  # >> tao mot dic rong
tel = {"jack": 4098, "sage": 4139}  # >> create dic with values
tel["guido"] = 4127  # >> add 1 key and value
del tel["jack"]  # >> delete with key
print(tel.keys())  # >> show the keys
print(tel.values())  # >> show the values
print("guido" in tel)  # >> check key is exist

# dict() create dic with list or tuple
d1 = dict([("sape", 4139), ("guido", 4127), ("jack", 4098)])  # >>create dic
d2 = dict(sape=4139, guido=4127, jack=4098)  # >> create dic
d3 = dict([(x, x ** 2) for x in (2, 4, 6)])  # >>{2:4,4:16,6:36} create dic by use a list comprehension
print(d1)
print(d2)
print(d3)
###5.6 Loop skill
# When loop through dictionary, keys and corresponding values can be show at the same time with method iteritems().
knights = {"gallahad": "the pure", "robin": "the brave"}
for k, v in knights.items():
    print(k, v)
# >> gallahad the pure
#     robin the brave

# When loop through a List,  get index and corresponding value at the same time
#   with method enumerate()
for i, v in enumerate(["tic", "tac", "toe"]):
    print(i, v)

# When Loop through two list or more at the same time, use method zip()
questions = ["name", "quest", "favorite color"]
answers = ["lancelot", "the holy grail", "blue"]
for q, a in zip(questions, answers):
    print("What is your {}? It is {}".format(q, a))
# Can be use reversed() or sorted() in list
for i in reversed(range(1, 10, 2)):
    print(i)
for f in sorted(set(basket)):
    print(f)

###5.7 Bàn thêm về điều kiện
# So sánh có thể nối được với nhau a < b==c
# Có thể gán kqua của một phép so sánh hoặc một Boolean vào một biến
s1 = ""
s2 = "hello"
s3 = "world"
non_null = s1 or s2 or s3
print(non_null)  # >> in ra giá trị khác null (s2)

###5.8 So sánh dãy và các kiểu khác
print("-" * 50)
# đầu tiên hai phần tử đầu được so sánh, và nếu khác nhau thì kqua sẽ đc xác định
#       nếu bằng nhau thì hai phần tử kế tiếp sẽ đc so sánh và cứ thế cho đến cuối 1 dãy
print("1.", (1, 2, 3) < (1, 2, 4))  # >> True
print("2.", [1, 2, 3,3] < [1, 2, 4,2])  # >>True
print("3.", "ABC" < "C" < "Pascal" < "Python")  # >> True
print("4.", (1, 2, 3, 4) < (1, 2, 4))  # >>True
print("5.", (1, 2) < (1, 2, -1))  # True
print("6.",(1,2,3)==(1.0,2.0,3.0)) #True

#Chú ý: ở python3 không thể so sánh đối tượng khác kiểu.



