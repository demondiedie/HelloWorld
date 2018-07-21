"""4.7 BAN THEM VE DINH NGHIA HAM"""
##4.7.1 Gia tri thong so mac dinh

#Cac gia tri mac dinh duoc dinh gia tai noi
#  ham duoc dinh nghia trong pham vi dinh nghia
i = 5
def f(arg=i):
    print(arg)
i=6
f()
#>>>> 5

#Chu y: Giá trị mặc định chỉ được định giá một lần.

#Ví dụ:
def f(a,L=[]):
    L.append(a)
    return L
print(f(1)) #>>[1]
print(f(2)) #>>[1,2]
print(f(3)) #>>[1,2,3] Hàm này gộp các thông số truyền vào nó từ các lời gọi sau đó.

##4.7.2 Thông số từ khóa
# Các hàm cũng có thể được gọi theo thông số từ khóa như sau:
def parrot(voltage,state="a stiff",action="voom",type="Norwegian Blue"):
    print("This is action: ",action)
    print("This is voltage: ",voltage)
    print("this is type: ",type)
    print("this is state: ",state)

#parrot(1000)
#parrot(action="dance",voltage=200)
#parrot("a thousand",state="pushing up the daisies")
#parrot("first","second","third")

##Chú ý: thông số truyền vào có dạng **name sẽ nhận một Từ Điển
#        *name sẽ nhận một thông số chính quy và nhận một bô Tuple chứa các thông số vị trí sau danh sách thông số chính quy.
#        *name bắt buộc phải xuất hiền trước **name
#Ví dụ:
def cheeseshop(kind,*arguments,**keywords):
    print("--Do you have any",kind,"?")
    print("--I:m sorry,we:re all out of",kind)
    for arg in arguments:
        print(arg)
    print("-"*40)
    keys = keywords.keys()

    for kw in keys:
        print(kw,":",keywords[kw])

cheeseshop("Limburger","It:s very runny,sir","It's really very, VERY runny,sir",
           client ="Jonh",shopkeeper="Michael Palin",sketch="Cheese Shop Sketch")
print("-"*50)
##4.7.3 Danh sách thông số bất kỳ

#Một hàm có thể gọi với bất kì số thông số.Các thông số này sẽ được gói vào trong một bộ.
#Trước các thông số không xác định,không hoặc nhiều hơn các thông số chính quy có thể có mặt.
def fprintf(file,format,*args):
    file.write(format%args)

##4.7.4 Tháo danh sách thông số

#Ví dụ:
a = [3,6]
print(list(range(*a))) #Thêm dấu * để tháo các thông số ra khỏi một danh sách hoặc bộ

print("-"*50)
#Theo cùng một kiểu, từ điển có thể cung cấp các thông số từ khóa với toán tử **:
#Ví dụ:
def par(voltage,state="a stiff",action="voom"):
    print("--this parot is ",action)
    print("if you put",voltage," vol through it")
    print("E's",state,"!")
d={"voltage":4000,"state":"bleedin' demised","action":"VOOM"}
par(**d)
print("-"*50)

##4.7.5 Dạng lambda
#Với từ khóa lambda, các hàm vô danh(anonymous function) có thể được tạo ra.Ví dụ: lambda a,b:a+b
#Dạng lambda có thể được dùng tại bất kì nơi nào cần đối tượng hàm.
#Cú pháp của chúng giới hạn ở một biểu duy nhất.Là cách viết gọn của một định nghĩa hàm bình thường.
#Dạng lambda có thể tham chiếu các biến từ phạm vi chứa nó:
def make_incrementor(n):
    return lambda a:a+n
f = make_incrementor(2) # truyền vào giá trị n = 2
#print(f())
print(f(1)) #truyền vào giá trị a = 1
print(f(99)) # a=3
#vd2:
i = lambda x,y:x+y
print(i(1,4))

##4.7.6 Chuỗi tài liệu




