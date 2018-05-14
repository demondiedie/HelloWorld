# input_x = input("Nhap du lieu: ")
# print(f"gia tri vua nhap:{input_x}")

print("yahoo!" if 3 > 4 else "shit!")

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
li.append("a")
li.append("b")
print(li)
li.pop(1)
del li[1]
li.remove("a")
li2 = li[:]
li.insert(1, 34)
li = li + li2
print(li)
print(len(li))
t = (1, 2, 3, "a")

a, b, c = (1, 2, 3)
a=2
print(a)
# kieu du lieu tu dien

dic ={"one":1,"two":2,"three":3}


dic.setdefault("five",5)
dic.update({"four":4})
print(dic.values())
dic.setdefault("five",6)
dic["seven"]=7
del dic["one"]
print(dic)

# kieu tap hop set
se = {1,1,2,2,3,4}

se2 = {2,3,4,5}
print(se | se2)
print(se-se2)
print(se^se2)
print(se>=se2)
print(2 in se)

# LUONG DIEU KHIEN VA KIEU KHA LAP

x_dic = dic.keys()
#for i in x_dic:
#   print(i),