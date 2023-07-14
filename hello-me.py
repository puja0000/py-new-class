import random
a_score=0
b_score=0
for i in range(1,5,1):
    user=int(input("enter a guess number"))
    computer=int(random.randint(0,9))
    print ("computer :"+str(computer))
    if user>computer:
        a_score+=10
        print(a_score)
    elif user<computer:
        b_score+=10
        print(b_score)
    else:
        print("equal")

if a_score>b_score:
    print("user won")
elif a_score<b_score:
    print("computer won")
else:
    print("equal")

 



