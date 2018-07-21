"""7.VÀO VÀ RA"""
#Có nhiều cách để thể hiện đầu ra của một chương trình.Dữ liệu có thể được in ra ở dạng người đọc được,
#   hoặc viết vào một tập tin để dùng sau này.

###7.1 Định dạng ra đẹp hơn
s = "Hello, world."
print(repr(s))
print(str(s))

for x in range(1,11):
    print(repr(x).rjust(3),repr(x*x).rjust(4),repr(x*x*x).rjust(5))

for x in range(1,11):
    print("%3d %4d %10d"%(x,x*x,x*x*x))

# rjust() : canh phải một chuỗi vào trong trường với độ rộng xác định bằng cách thêm khoảng trông vào bên trái
# Các phương thức khác gồm ljust() và center()

# zfill() đệm không vào bên trái một chuỗi số.
print("12".zfill(5))
print("3.14".zfill(10))

table = {"Sjoerd":4127,"Jack":4098}
print("Jack:%(Jack)d; Sjoerd:%(Sjoerd)d"%table)

###7.2 Đọc và viết tập tin
# open() trả về một đối tượng tập tin, và thường được dùng với hai thông số: open(filename,mode)




