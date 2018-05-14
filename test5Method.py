"""
def fib(n): #write Fibonacci series up to n
    #Print a Fibonacci serices up to n
    a,b = 0,1
    while b<n:
        print(b,end=" ")
        a,b=b,a+b
#Now call the funnction we just defined:
f = fib
f(100)
print("\n",fib(0))
print("bbbb")

def fb(n):
    listFB = []
    a,b=0,1
    while b<n:
        listFB.append(str(b))
        a,b=b,a+b
    return listFB
a = fb(100)

print(','.join(a))
"""
#####################################################
"""
i = 5
def f(ar=i):
    print(ar)

i=6
f() #in ra 5 vi` ham da nhan gia tri bang 5 tu truoc
f(7) # in ra 7
"""


