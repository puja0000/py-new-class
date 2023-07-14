def demo(operator,num_one,num_two):
    a=num_one
    b=num_two
    operator=input("enter operator")
    if operator=='+':
        print(a+b)
    elif operator=='-':
        print(a-b)
    elif operator=='*':
        print (a*b)
    elif operator=='/':
        print(a/b)

demo('+',7,8)
demo('-',20,10)
demo('*',100,100)
demo('/',20,2)