x = 10
if x > 5:
    print("x is totally bigger than  5")
elif x < 5:
    print("x is smaller than 5")
else:
    print("x is indeed 5")

# for animal in ["dog","cat","mouse"]:
#  print(f"{animal} is best")
#   print("{} is best".format(animal))

# for i in range(4):
#    print("")
#    for j in range(4-i):
#        print("*",end=" ")
"""
try:
    a = ["dog", 1, "cat"]
    a = iter(a)
    print(a)
    print(list(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    raise IndexError("this is an index error")
except IndexError as e:
    print(IndexError)
except (TypeError,NameError):
    print(TypeError,NameError)
else:
    print("all good")
finally:
    print("We can clean up resources here")
"""

# CLASS

def add(x,y):
    print("x is {} and y is {}".format(x,y))
    return x+y

def var(*var):
    return var
print(var(1,2,3,4))

def sw(x,y):
    return y,x
x=1
y=2
x,y=sw(x,y)
print(x,y)
def create_adder(x):
    def adder(y):
        return x+y
    return adder

add_10 = create_adder(10)
print(add_10(3))

print((lambda x:x>2)(3))
print((lambda x,y:x+y)(2,1))

print(list(map(add_10,[1,2,3])))
print(list(map(max,[1,2,3],[4,2,1])))
print(max([1,2,3],[0,1,0]))

print([add_10(i) for i in [1,2,3]])
print([x for x in [1,2,3,4,5,11] if x>3])



