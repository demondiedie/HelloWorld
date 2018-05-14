# BAI 1
# print([i for i in range(2000,3200) if (i%7==0) and (i%5!=0)])
"""j=[]
for i in range(2000,3201):
    if (i%7==0) and (i%5!=0):
        j.append(str(i))

print(','.join(j))"""

# BAI 2
"""x = input("Nhap so can tinh giai thua: ")
kq = 1
for i in range(int(x)):
   kq=(i+1)*kq
print("kqua giai thua cua {} la {}".format(x,kq))
print(f"kqua giai thua cua {x} la {kq}")
print("kqua giai thua cua %s la %s"%(x,kq))
"""
"""x = 3
def fact(x):
    if x ==0:
        return 1
    return x*fact(x-1)
print(fact(x))"""

# BAI 3
"""
n = 8
dic = {}
for i in range(1,n+1):
   dic[i]=i*i
print(dic)
"""
# BAI 4
"""
x =input("nhap vao gia tri")
print (x)
l = x.split(' ')
t = tuple(l)
print(l)
print(t)
"""
# BAI 5
"""class InHoa:
    def __init__(self):
        self._s = ""
        self.binhPhuong = None
    def getString(self):
        self._s = input("Nhap chuoi:")
    def printString(self):
        print(self._s.upper())
    def tinhBinhPhuong(self,giaTriBinhPhuong):
        self.binhPhuong = giaTriBinhPhuong**2
        return self.binhPhuong


s = InHoa()
s.getString()
s.printString()
print(s.tinhBinhPhuong(3))
"""

# BAI 6
# print(abs.__doc__)
# print(int.__doc__)
# print(input.__doc__)
# def square(num):
#    return num**2

# print(square.__doc__)

# Bai 8
"""class Member:
    name = "Member"
    age = 0

    def __init__(self, name=None, age=0):
        self.name = name
        self.age = age


m = Member("AC", 10)
# m.setNameAge("Tiep", 29)

print(f"{m.name} : {m.age}")
n = Member()
n.name = "TIEP"
n.age = 29
print("%s name is %s"%(Member.name,n.name))
"""

# Bai 9
"""import math

d = [100,150,180]
q = []
c = 50
h = 30
#i = input("nhap vao day so: ")
#d = i.split(",")

for j in range(len(d)):
    q.append(str(int(round(math.sqrt((2*c*d[j])/h)))))

print(','.join(q))
print()
"""
# bai 10
x = 3
y = 5
"""dimen = [3,5]
rowNum = dimen[0]
colNum = dimen[1]
print(dimen)
multilist = [[0 for col in range(colNum)]for row in range(rowNum)]
for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col]=row*col
print(multilist)
"""
ls = list()
print(ls)
for row in range(3):
    for col in range(5):
        ls[row][col]=row*col
print(ls)