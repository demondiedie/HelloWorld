"""word = 'HelpA'
str = 'x' + word[1:]
print(word)
print(str)
print(word[2:1]+"a")
"""
"""
for i in range(10):
    try:
        x = int(input("Plz enter an integer: "))
        if x < 0:
            x = 0
            print("negative changed to %s"%x)
        elif x == 0 :
            print("zero")
        elif x==1:
            print("single")
        elif x >1:
            print("more")
        else:
            print("more")
    except:
        print("owari")
        break
"""
"""
a = ["cat","widow","human"]
for x in a[:]:
    if not x=="widow": a.insert(3,x)
print(a)
print(2==True)

a,b=0,1
while b<20:
    print(b,end=" ")
    a,b=b,a+b


for i in range(0,10,2):
    print(i)


for n in range(2,10):
    for x in range(2,n):
        if n%x==0:
            print(n,"equals",x,"*",n/x)
            break
    else: # Vong lap di qua ma khong tim ra mot yeu to
        print(n,"is a prime number")

"""




