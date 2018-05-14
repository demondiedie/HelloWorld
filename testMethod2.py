"""
def ask_ok(prompt,retries=4,complaint='yes or no,please!'):
    while True:
        ok = input(prompt)
        if ok in ("y","ye","yes"):return True
        if ok in ("n","no","nop","nope"): return False
        retries = retries -1
        if retries<0:raise IOError
        print(complaint)

ask_ok("Do you really want to quit?",2)
"""
"""
def f1(a,L=[]): # gia tri mac dinh chi duoc dinh gia mot lan
    L.append(a)
    return L
print(f1(1)) # >> in ra [1]
print(f1(3)) #>>>> in ra [1,3]

def f(a,L=None):
    if L is None:
        L = []
    L.append(a)
    return L
print(f(1))
print(f(3))
"""

# def parrot(voltage,state="a stiff",action ="voom",type="Norwegian Blue"):
#     print("--This parrot wouldn't",action,)
#     print("if you put",voltage,"volts through it")
#     print("--Lovely plumage,the",type)
#     print("--It's",state)
# #nhung cach goi hop le
# parrot(1000)
# parrot(action="V0000M",voltage=1000000)
# parrot("a hundred","bereft of life","jump")
# parrot(voltage=5.1)
# # nhung cach goi khong hop le:
# parrot() # required argument missing
# parrot(voltage=5.0,"dead") #non-keyword argument following keyword
# parrot(110,voltage=220) # duplicate value for argument
# parrot(actor="john") # unknown keyword

##########################################
# def cheeseshop(kind,*arguments,**keywords):
#     print("--Do you have any",kind,"?")
#     print("--i'm sorry, we're all out of",kind)
#     for arg in arguments: print(arg) # in ra danh sach
#     print("-"*40)
#     key = keywords.keys() #dang dictionary
#
#     for kw in key: print(kw,":",keywords[kw])
#
# cheeseshop("limburger","it's very runny, sir.",
#            "It's really very, VeRY runny,sir",
#            "xin chao toi la tiep",
#            client="john chee",
#            shopkeeper = "michael palin",
#            sketch = "cheese shop sketch")

############################################################
# import random
#
# A = []
# a = []
# for i in range(10):
#     A.append(random.randrange(100))
# print(A)
# A.sort()
# print(A)
# j = len(A)-1
# for i in range(1,j,2):
#     tem = A[i]
#     A[i]=A[i+1]
#     A[i+1]=tem
# print(A)

########################################
# def chao(ten):
#     """ham nay se in ra
#      ten nguoi duoc nhap vao"""
#     print("xin chao "+ten+" !")
#
#
# print(chao.__doc__)
#############################################

# def make_incrementor(n):
#     return lambda x: x+n
# f=make_incrementor(42)
# print(f(0))
# print(f(1))

################################################

