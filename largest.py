a=int(input("enter first number"))
b=int(input("enter seond number"))
c=int(input("enter third number"))
for i in range(1,5,8):
    if a>b and a>c :
         print("a is largest")
    elif b>a and b>c:
        print("b is largest") 
    elif c>a and c>b:
            print("c is largest")
print("your program ended")               