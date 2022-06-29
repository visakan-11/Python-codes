def hello():
    print("Hello World")
print("Before Function")
hello()
print("After Function")
print("\n")
def myfun1(*A):
    for arg in A:
        print(arg,end=" ")

def myfun2(**B):
    for key,value in B.items():
        print("%s == %s" %(key,value))

myfun1('Hello','Welcome','to','GeeksforGeeks')
print()
myfun2(first='Geeks',mid='for',last='Geeks')

