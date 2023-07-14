 
p=int(input("enter first number"))
u=float(input("enter first number"))
operator=input("enter operator")
if operator=='+':
   print(p+u)
elif operator=='-':
    print(p-u)
elif operator=='*':
    print (p*u)
elif operator=='/':
    print(p/u)
else:
    print ("math error")
